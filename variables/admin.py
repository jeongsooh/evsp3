from django.contrib import admin
from .models import Variables

# Register your models here.

class VariablesAdmin(admin.ModelAdmin):
  list_display = ('variable', 'group', 'value',)

admin.site.register(Variables, VariablesAdmin)
