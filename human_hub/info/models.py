from django_resized import ResizedImageField

from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutPage(models.Model):
    text_1 = models.TextField(_("About page text (frst prt"), default="", blank=True)
    image_1 = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)
    text_2 = models.TextField(_("About page text (scnd prt"), default="", blank=True)
    image_2 = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)

class ContactsPage(models.Model):
    text = models.TextField(_("Contacts page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)


class DiscountsPage(models.Model):
    text = models.TextField(_("Discounts page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)


class SizingPage(models.Model):
    text = models.TextField(_("Sizing page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)


class ShippingPage(models.Model):
    text = models.TextField(_("Shipping page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)


class RefundPage(models.Model):
    text = models.TextField(_("Refund page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)


