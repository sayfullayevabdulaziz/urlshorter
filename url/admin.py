import imp
from django.contrib import admin
from .models import UrlModel, ReportLinkModel, ContactModel
# Register your models here.

class UrlModelAdmin(admin.ModelAdmin):
    list_display = ['url', 'slug', 'counter']


class DateAdmin(admin.ModelAdmin):
    list_display = ['url']
    readonly_fields = ['created_at']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['created_at']



admin.site.register(UrlModel, UrlModelAdmin)
admin.site.register(ReportLinkModel, DateAdmin)
admin.site.register(ContactModel, ContactAdmin)