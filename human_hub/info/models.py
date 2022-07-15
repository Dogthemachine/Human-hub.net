from django_resized import ResizedImageField

from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutPage(models.Model):
    text_1 = models.TextField(_("About page text (frst prt"), default="", blank=True)
    image_1 = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)
    text_2 = models.TextField(_("About page text (scnd prt"), default="", blank=True)
    image_2 = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if AboutPage.objects.count() != 1:
            self.delete()


class ContactsPage(models.Model):
    text = models.TextField(_("Contacts page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if ContactsPage.objects.count() != 1:
            self.delete()


class DiscountsPage(models.Model):
    text = models.TextField(_("Discounts page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if DiscountsPage.objects.count() != 1:
            self.delete()


class SizingPage(models.Model):
    text = models.TextField(_("Sizing page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if SizingPage.objects.count() != 1:
            self.delete()


class ShippingPage(models.Model):
    text = models.TextField(_("Shipping page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if ShippingPage.objects.count() != 1:
            self.delete()


class RefundPage(models.Model):
    text = models.TextField(_("Refund page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if RefundPage.objects.count() != 1:
            self.delete()


class TermsPage(models.Model):
    terms = models.TextField(_("Terms of use"), default="", blank=True)
    privacy = models.TextField(_("Privacy policy"), default="", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if TermsPage.objects.count() != 1:
            self.delete()


