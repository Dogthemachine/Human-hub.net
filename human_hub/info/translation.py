from modeltranslation.translator import translator, TranslationOptions

from info.models import AboutPage, ContactsPage, DiscountsPage, SizingPage, ShippingPage, RefundPage


class AboutPageTranslationOptions(TranslationOptions):
    fields = ('text_1', 'image_1', 'text_2', 'image_2',)


class ContactsPageTranslationOptions(TranslationOptions):
    fields = ('text', 'image',)


class DiscountsPageTranslationOptions(TranslationOptions):
    fields = ('text', 'image',)


class SizingPageTranslationOptions(TranslationOptions):
    fields = ('text', 'image',)


class ShippingPageTranslationOptions(TranslationOptions):
    fields = ('text', 'image',)


class RefundPageTranslationOptions(TranslationOptions):
    fields = ('text', 'image',)


translator.register(AboutPage, AboutPageTranslationOptions)

translator.register(ContactsPage, ContactsPageTranslationOptions)

translator.register(DiscountsPage, DiscountsPageTranslationOptions)

translator.register(SizingPage, SizingPageTranslationOptions)

translator.register(ShippingPage, ShippingPageTranslationOptions)

translator.register(RefundPage, RefundPageTranslationOptions)
