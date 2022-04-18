from django.contrib import admin
from .models import Book


class BookList(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'description', 'rating')
    list_filter = ('title', 'author', 'year', 'rating')
    search_fields = ('title', 'author', 'description')
    ordering = ['year']


admin.site.register(Book, BookList)

