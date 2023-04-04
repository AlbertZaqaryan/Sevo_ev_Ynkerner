from .models import Category, SubCategory
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)