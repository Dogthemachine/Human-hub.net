from modeltranslation.admin import TranslationAdmin

from django.contrib import admin

from info.models import AboutPage, ContactsPage, DiscountsPage, SizingPage, ShippingPage, RefundPage


class AboutPageAdmin(TranslationAdmin):
    list_display = ('text_1', 'image_1', 'text_2', 'image_2',)


class ContactsPageAdmin(TranslationAdmin):
    list_display = ('text', 'image',)


class DiscountsPageAdmin(admin.ModelAdmin):
    list_display = ('text', 'image',)


class SizingPageAdmin(admin.ModelAdmin):
    list_display = ('text', 'image',)


class ShippingPageAdmin(admin.ModelAdmin):
    list_display = ('text', 'image',)


class RefundPageAdmin(TranslationAdmin):
    list_display = ('text', 'image',)


admin.site.register(AboutPage, AboutPageAdmin)

admin.site.register(ContactsPage, ContactsPageAdmin)

admin.site.register(DiscountsPage, DiscountsPageAdmin)

admin.site.register(SizingPage, SizingPageAdmin)

admin.site.register(ShippingPage, ShippingPageAdmin)

admin.site.register(RefundPage, RefundPageAdmin)

