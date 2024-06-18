from django.contrib import admin
from .models import Product, Comment

# Register your models here.
admin.site.register(Product)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'description', 'date_time_created')

