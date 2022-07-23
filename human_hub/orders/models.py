from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from showcase.models import Balance, Items, Sizes, Config


class Orders(models.Model):
    name = models.CharField(_("first name"), max_length=70)
    last_name = models.CharField(_("last name"), max_length=70)
    phone = models.CharField(_("phone"), max_length=32, db_index=True)
    comment = models.TextField(_("comment"), default="", blank=True)
    email = models.EmailField(_("email"), max_length=254, null=True, blank=True)
    lang_code = models.CharField(_("lang code"), default="ru", blank=True, max_length=2)
    delivered = models.BooleanField(_("delivered"), default=False)
    paid = models.BooleanField(_("paid"), default=False)
    date_of_delivery = models.DateField(_("date_of_delivery"), blank=True, null=True)
    delivery_method = models.CharField(_("delivery_method"), default="", blank=True, max_length=70)
    payment_method = models.CharField(_("payment_method"), default="", blank=True, max_length=70)
    liqpay_wait_accept = models.BooleanField(_("LiqPay wait accept"), default=False)
    wfp_status = models.CharField(_("WFP status"), max_length=512, default="", blank=True)
    ttn = models.IntegerField(_("TTN"), default=0)
    packed = models.BooleanField(_("Packed"), default=False)
    added = models.DateTimeField(_("added"), auto_now_add=True)

    class Meta:
        ordering = ("-added",)
        verbose_name = _("Orders")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return u"%s" % self.name

    def get_total_price_grn(self):
        items = OrderItems.objects.filter(order=self)
        sum = 0

        for i in items:
            sum += i.price * i.amount

        return sum

    def get_total_price(self, request):
        sum = self.get_total_price_grn()
        if request.session["valuta"] == "grn":
            pass
        else:
            config = Config.objects.get()
            rate = 1
            if request.session["valuta"] == "usd":
                rate = config.dollar_rate
            if request.session["valuta"] == "eur":
                rate = config.euro_rate
            sum = round(sum / rate, 2)

        return sum


    def get_total_paid(self):
        items = Payment.objects.filter(order=self)
        sum = 0

        for i in items:
            sum += i.amount

        return sum

    def get_remaining_amount(self):
        return self.get_total_price_grn() - self.get_total_paid()

    def get_number(self):
        return self.id


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(_("amount"))
    price = models.PositiveIntegerField(_("price"), default=0)
    added = models.DateTimeField(_("added"), auto_now_add=True)

    class Meta:
        ordering = ("added",)
        verbose_name = _("Order item")
        verbose_name_plural = _("Order items")

    def __str__(self):
        return u"%s" % self.order


class Payment(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(_("amount"))
    comment = models.CharField(_("comment"), max_length=512)
    token = models.CharField(_("liqpay token"), max_length=512, blank=True)
    sender_phone = models.CharField(_("liqpay sender phone"), max_length=64, blank=True)
    added = models.DateTimeField(_("added"), auto_now_add=True)


class PaymentRaw(models.Model):
    data = models.TextField(_("data"))
    sign = models.TextField(_("sign"))
    data_decoded = models.TextField(_("data decoded"), default="", blank=True)
    added = models.DateTimeField(_("added"), auto_now_add=True)


class Cart(models.Model):
    session_key = models.CharField(_("name"), max_length=32)
    added = models.DateTimeField(_("added"), auto_now_add=True)

    class Meta:
        ordering = ("added",)
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return u"%s" % self.session_key

    def get_total(self):
        items = CartItem.objects.filter(cart=self)
        total = 0
        for item in items:
            total += item.item.price * item.amount
        return total

    def get_items_count(self):
        stock = Stocks.objects.filter(
            type=1,
            action_begin__lte=timezone.datetime.today(),
            action_end__gte=timezone.datetime.today(),
        ).order_by("-id")[:1]

        message = ""

        if stock:
            count = 0

            cart_items = CartItem.objects.filter(cart=self).order_by("-item__price")

            for i in cart_items:
                count += i.amount

            items = count // (stock[0].items_count + 1)

            sum = 0

            discounted_items = []

            for i in cart_items:
                for j in range(0, i.amount):
                    discounted_items.append(i.item.price)

            n = 0
            for i in discounted_items:
                n += 1
                if n % (stock[0].items_count + 1) == 0:
                    sum += i

            self.discount_stocks = sum
            self.comment = gettext("Your discount is %s UAH.") % sum
            self.save()

            if sum:
                message = gettext(
                    "You have %(items)s discounted items for %(sum)s UAH."
                ) % {"items": items, "sum": sum}

            modulo = count % (stock[0].items_count + 1)
            if modulo == stock[0].items_count:
                message += gettext("You can add one more item and get a discount.")
                # message += stock.description

        return message



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()

    def check_avail(self):
        balance = Balance.objects.get(item=self.item, size=self.size)

        if balance.amount >= self.amount:
            return True
        else:
            return False


@receiver(post_save, sender=OrderItems)
def update_balance_on_order(sender, instance, created, **kwargs):
    if created:
        balance = instance.balance
        balance.amount = balance.amount - instance.amount
        balance.save()


@receiver(post_delete, sender=OrderItems)
def update_balance_or_order_delete(sender, instance, **kwargs):
    balance = instance.balance
    balance.amount = balance.amount + instance.amount
    balance.save()

