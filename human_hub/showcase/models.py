from django_resized import ResizedImageField
from solo.models import SingletonModel


from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _



class Categories(models.Model):
    name = models.CharField(_("name"), max_length=70)
    details = models.TextField(_("details"), blank=True)
    title_tag = models.CharField(_("title tag"), max_length=70, blank=True, default="")
    description_tag = models.CharField(_("description tag"), max_length=280, blank=True, default="")
    sequence = models.PositiveSmallIntegerField(_("sequence"), default=0)
    showcase_displayed = models.BooleanField(_("showcase_displayed"), default=True)

    class Meta:
        ordering = ("sequence",)
        verbose_name = _("Categories")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return u"%s" % self.name

    def get_items(self):
        return Items.objects.filter(category=self)

    def get_first2items(self):
        return Items.objects.filter(category=self).order_by("-added")[:2]


    def get_rest_items(self):
        return Items.objects.filter(category=self).order_by("-added")[2:]


class Items(models.Model):
    name = models.CharField(_("name"), max_length=250)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = ResizedImageField(size=[2500, 2500], upload_to="photos/%Y/%m/%d")
    image_small = ResizedImageField(size=[300, 300], crop=["middle", "center"], upload_to="small_photos/%Y/%m/%d", editable=False,)
    description = models.TextField(_("how it fits"), blank=True, default="")
    details = models.TextField(_("details"), blank=True, default="")
    price = models.PositiveSmallIntegerField(_("price"), default=0)
    price_description = models.CharField(_("price_description"), max_length=250, default=_("Grn."))
    views = models.PositiveIntegerField(_("views"), default=0)
    views_today = models.PositiveIntegerField(_("views today"), default=0)
    views_month = models.CharField(_("views month"), default=0, max_length=512)
    showcase_displayed = models.BooleanField(_("showcase_displayed"), default=True)
    showcase_new = models.BooleanField(_("showcase_new"), default=True)
    title_tag = models.CharField(_("title tag"), max_length=70, blank=True, default="")
    description_tag = models.CharField(_("description tag"), max_length=280, blank=True, default="")
    added = models.DateTimeField(_("added"), auto_now_add=True)

    class Meta:
        ordering = ("-views",)
        verbose_name = _("items")
        verbose_name_plural = _("items")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.was_views_today = self.views_today

    def __str__(self):
        return u"%s (%s) (%s)" % (self.name, self.category.name, self.description)


    def get_balance(self):
        return Balance.objects.filter(item=self)

    def get_amount(self):
        balances = Balance.objects.filter(item=self)
        for balance in balances:
            if balance.amount > 0:
                return True
        return False

    def sorting(self):
        return (
            Balance.objects.filter(item=self).aggregate(Sum("amount"))
            * self.views_per_month
        )


class Sizes(models.Model):
    name = models.CharField(_("name"), max_length=20)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField(_("description"), blank=True, default="")
    sequence = models.PositiveSmallIntegerField(_("sequence"), default=0)

    class Meta:
        ordering = ("sequence",)
        verbose_name = _("Sizes")
        verbose_name_plural = _("Sizes")

    def __str__(self):
        return u"%s" % self.name


class Photo(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    image = ResizedImageField(size=[2500, 2500], upload_to="photos/%Y/%m/%d")
    image_small = ResizedImageField(
        size=[300, 300],
        crop=["middle", "center"],
        upload_to="small_photos/%Y/%m/%d",
        editable=False,
    )
    added = models.DateTimeField(_("added"), auto_now_add=True)

    class Meta:
        ordering = ("added",)
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def save(self, *args, **kwargs):
        if not self.image._committed:
            self.image_small = self.image.file
        super().save(*args, **kwargs)

    def __str__(self):
        return u"%s - %s" % (self.item.name, self.added)


class Balance(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    amount = models.IntegerField(_("amount"), default=0)

    class Meta:
        ordering = ("id",)
        verbose_name = _("Amount")
        verbose_name_plural = _("Amount")

    def __str__(self):
        return u"%s - %s - %s" % (self.item.name, self.size.name, self.amount)


class BalanceLog(models.Model):
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    old_value = models.IntegerField(_("old value"))
    new_value = models.IntegerField(_("new value"))
    arrival = models.BooleanField(_("arrival"), default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    change_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-change_time",)
        verbose_name = _("Balance log")
        verbose_name_plural = _("Balance logs")

    def __str__(self):
        return "%s - %s" % (self.balance, self.change_time)


class Banner(models.Model):
    image_showcase = ResizedImageField(size=[2000, 300], upload_to="photos/%Y/%m/%d")
    image_category = ResizedImageField(size=[2000, 300], upload_to="photos/%Y/%m/%d")

    class Meta:
        verbose_name = _("Banners")
        verbose_name_plural = _("Banners page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if Banner.objects.count() != 1:
            self.delete()


class Config(SingletonModel):
    dollar_rate = models.DecimalField(
        _("dollar rate"), max_digits=5, decimal_places=2, default=1
    )
    euro_rate = models.DecimalField(
        _("euro rate"), max_digits=5, decimal_places=2, default=1
    )
    price_description = models.CharField(
        _("price_description"), max_length=250, default=gettext("Grn.")
    )
    price_description_usd = models.CharField(
        _("price_description"), max_length=250, default=gettext("Usd.")
    )
    price_description_eur = models.CharField(
        _("price_description"), max_length=250, default=gettext("Eur.")
    )
    static = models.CharField(
        _("static url"), max_length=250, default="https://catcult.club/static/"
    )
    media = models.CharField(
        _("media url"), max_length=250, default="https://catcult.club/media/"
    )
    merchant_account = models.CharField(
        _("merchant account"), max_length=64, default=""
    )
    merchant_secret = models.CharField(_("merchant secret"), max_length=128, default="")
    merchant_domain_name = models.CharField(
        _("merchant domain name"), max_length=64, default=""
    )
    service_url = models.CharField(_("service URL"), max_length=512, default="")

    class Meta:
        ordering = ("dollar_rate",)
        verbose_name = _("Config")
        verbose_name_plural = _("Config")

    def __str__(self):
        return u"%s" % self.dollar_rate


@receiver(post_save, sender=Items)
def create_item_balance(instance, created, **kwargs):
    if created:
        category = instance.category
        sizes = Sizes.objects.filter(categories=category)
        for size in sizes:
            balance = Balance(item=instance, size=size)
            balance.save()




