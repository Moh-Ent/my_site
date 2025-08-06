from django.contrib import admin
from base.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'created_date')
    search_fields = ('name', 'subject', 'message')


admin.site.register(Contact, ContactAdmin)