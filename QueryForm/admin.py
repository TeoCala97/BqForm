from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ('qname','select','fecha')

admin.site.register(Form, FormAdmin)
