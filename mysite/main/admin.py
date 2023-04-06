from django.contrib import admin
from .models import SliderActive, Category, SubCategory, Contact
# Register your models here.

admin.site.register(SliderActive)
admin.site.register(Category)
admin.site.register(SubCategory)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'subject']
