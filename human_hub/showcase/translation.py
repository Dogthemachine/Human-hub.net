from modeltranslation.translator import translator, TranslationOptions

from showcase.models import Items, Photo, Categories, Sizes, Balance


class ItemsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'details', 'price_description', 'title_tag', 'description_tag',)


class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name', 'details', 'title_tag', 'description_tag',)


class SizesTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


translator.register(Items, ItemsTranslationOptions)

translator.register(Categories, CategoriesTranslationOptions)

translator.register(Sizes, SizesTranslationOptions)
