from django.contrib import admin

from applications.administrator.models import HtmlMailTemplates

# Register your models here.
class HtmlMailTemplatesAdmin(admin.ModelAdmin):
    list_display = ['ht_id', 'ht_name', 'ht_subject', 'ht_active']
    list_per_page = 10

admin.site.register(HtmlMailTemplates, HtmlMailTemplatesAdmin)