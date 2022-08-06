from modeltranslation.admin import TranslationAdmin

from django.contrib import admin

from info.models import (
    AboutPage,
    ContactsPage,
    DiscountsPage,
    SizingPage,
    ShippingPage,
    RefundPage,
    TermsPage,
    InfoPages,
)


class AboutPageAdmin(TranslationAdmin):
    list_display = ('text_1', 'image_1', 'text_2', 'image_2',)


class ContactsPageAdmin(TranslationAdmin):
    list_display = ('text', 'image',)


class DiscountsPageAdmin(TranslationAdmin):
    list_display = ('text', 'image',)


class SizingPageAdmin(TranslationAdmin):
    list_display = ('text', 'image',)


class ShippingPageAdmin(TranslationAdmin):
    list_display = ('text', 'image',)


class RefundPageAdmin(TranslationAdmin):
    list_display = ('text', 'image',)


class TermsPageAdmin(TranslationAdmin):
    list_display = ('terms', 'privacy',)


class InfoPagesAdmin(TranslationAdmin):
    list_display = ('tag', 'text_1', 'image_1', 'text_2', 'image_2',)


admin.site.register(AboutPage, AboutPageAdmin)

admin.site.register(ContactsPage, ContactsPageAdmin)

admin.site.register(DiscountsPage, DiscountsPageAdmin)

admin.site.register(SizingPage, SizingPageAdmin)

admin.site.register(ShippingPage, ShippingPageAdmin)

admin.site.register(RefundPage, RefundPageAdmin)

admin.site.register(TermsPage, TermsPageAdmin)

admin.site.register(InfoPages, InfoPagesAdmin)
