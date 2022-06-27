from django_resized import ResizedImageField

from django.db import models
from django.utils.translation import gettext_lazy as _


class Info(models.Model):
    topic = models.CharField(_("topic"), max_length=50, unique=True, db_index=True)
    title = models.CharField(_("name"), max_length=250, blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)
    video = models.CharField(_("video"), max_length=1000, default="", blank=True)
    info = models.TextField(_("text"), default="", blank=True)
    title_tag = models.CharField(_("title tag"), max_length=70, blank=True, default="")
    description_tag = models.CharField(
        _("description tag"), max_length=280, blank=True, default=""
    )

    class Meta:
        verbose_name = _("Info")
        verbose_name_plural = _("Infos")

    def __str__(self):
        return u"%s" % self.topic


class AboutPage(models.Model):
    text = models.TextField(_("About page text"), default="", blank=True)
    image = ResizedImageField(size=[1500, 1500], upload_to="info", blank=True)


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


