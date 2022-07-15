from modeltranslation.admin import TranslationAdmin

from django.contrib import admin

from showcase.models import Items, Photo, Categories, Sizes, Balance, Banner, Config

from django.contrib.auth.models import Group


class PhotoInline(admin.TabularInline):
    model = Photo


class ItemsAdmin(TranslationAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'category', 'added', 'price', 'price_description', 'description',)


class CategoriesAdmin(TranslationAdmin):
    list_display = ('name', 'details', 'sequence',)


class SizesAdmin(admin.ModelAdmin):
    list_display = ('name', 'categories', 'description', 'sequence',)


class BalanceAdmin(admin.ModelAdmin):
    list_display = ('item', 'size', 'amount',)


class BannerAdmin(TranslationAdmin):
    list_display = ('image_showcase', 'image_category',)


class ConfigAdmin(TranslationAdmin):
    list_display = ('dollar_rate', 'euro_rate',)


admin.site.register(Items, ItemsAdmin)

admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Sizes, SizesAdmin)

admin.site.register(Balance, BalanceAdmin)

admin.site.register(Banner, BannerAdmin)

admin.site.register(Config, ConfigAdmin)

admin.site.unregister(Group)