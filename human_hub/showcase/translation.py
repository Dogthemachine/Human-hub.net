from modeltranslation.translator import translator, TranslationOptions

from showcase.models import Items, Photo, Categories, Sizes, Balance, Config, Banner


class ItemsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'details', 'price_description', 'title_tag', 'description_tag',)


class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name', 'details', 'title_tag', 'description_tag',)


class SizesTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


class ConfigTranslationOptions(TranslationOptions):
    fields = ('price_description', 'price_description_usd', 'price_description_eur',)


class BannerTranslationOptions(TranslationOptions):
    fields = ('image_showcase', 'image_category',)


translator.register(Items, ItemsTranslationOptions)

translator.register(Categories, CategoriesTranslationOptions)

translator.register(Sizes, SizesTranslationOptions)

translator.register(Config, ConfigTranslationOptions)

translator.register(Banner, BannerTranslationOptions)
