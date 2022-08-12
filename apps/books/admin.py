from django.contrib import admin
from apps.books.models import Editorial, Author, Book



class EditorialAdmin(admin.ModelAdmin):
    list_display = ('name',)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'nationality')
class BookAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'author', 'editorial', 'is_available')

admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)