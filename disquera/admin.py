from django.contrib import admin
from .models import Category, Post, Comment, Specification


class SpecificationInline(admin.TabularInline):
   model = Specification
   extra = 2


class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'status', 'created_at')

   inlines = [SpecificationInline]

   prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
