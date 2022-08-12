from django.contrib import admin
from apps.users.models import CustomUser, Borrow, Restore
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):

    # fieldsets = (
    #     *UserAdmin.fieldsets,  # original form fieldsets, expanded
    #     (                      # new fieldset added on to the bottom
    #         'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
    #         {
    #             'fields': (
    #                 'birthdate',
    #             ),
    #         },
    #     ),
    # )

    list_display = ('username','birthdate')

class BorrowAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'book')
class RestoreAdmin(admin.ModelAdmin):
    list_display = ('date', 'borrow')

admin.site.register(Borrow, BorrowAdmin)
admin.site.register(Restore, RestoreAdmin)
admin.site.register(CustomUser, CustomUserAdmin)