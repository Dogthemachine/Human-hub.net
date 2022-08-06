from django_resized import ResizedImageField

from django.db import models
from django.utils.translation import gettext_lazy as _


class InfoPages(models.Model):
    tag = models.CharField(_("tag"), max_length=20)
    text_1 = models.TextField(_("frst prt"), default="", blank=True)
    image_1 = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)
    text_2 = models.TextField(_("scnd prt"), default="", blank=True)
    image_2 = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    class Meta:
        verbose_name = _("Info pages")
        verbose_name_plural = _("Info pages")


class AboutPage(models.Model):
    text_1 = models.TextField(_("frst prt"), default="", blank=True)
    image_1 = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)
    text_2 = models.TextField(_("scnd prt"), default="", blank=True)
    image_2 = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    class Meta:
        verbose_name = _("About page")
        verbose_name_plural = _("About page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if AboutPage.objects.count() != 1:
            self.delete()


class ContactsPage(models.Model):
    text = models.TextField(_("Contacts page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    class Meta:
        verbose_name = _("Contacts page")
        verbose_name_plural = _("Contacts page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if ContactsPage.objects.count() != 1:
            self.delete()


class DiscountsPage(models.Model):
    text = models.TextField(_("Discounts page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    class Meta:
        verbose_name = _("Discounts page")
        verbose_name_plural = _("Discounts page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if DiscountsPage.objects.count() != 1:
            self.delete()


class SizingPage(models.Model):
    text = models.TextField(_("Sizing page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    class Meta:
        verbose_name = _("Sizing page")
        verbose_name_plural = _("sizing page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if SizingPage.objects.count() != 1:
            self.delete()


class ShippingPage(models.Model):
    text = models.TextField(_("Shipping page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    class Meta:
        verbose_name = _("Shipping page")
        verbose_name_plural = _("Shipping page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if ShippingPage.objects.count() != 1:
            self.delete()


class RefundPage(models.Model):
    text = models.TextField(_("Refund page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    class Meta:
        verbose_name = _("Refund page")
        verbose_name_plural = _("Refund page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if RefundPage.objects.count() != 1:
            self.delete()


class TermsPage(models.Model):
    terms = models.TextField(_("Terms of use"), default="", blank=True)
    privacy = models.TextField(_("Privacy policy"), default="", blank=True)

    class Meta:
        verbose_name = _("Terms page")
        verbose_name_plural = _("Terms page")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if TermsPage.objects.count() != 1:
            self.delete()


