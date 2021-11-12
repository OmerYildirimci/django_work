from django.contrib import admin
from .models import Category,Blog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {
   'slug': ('name', ),
}
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','image','description','category')