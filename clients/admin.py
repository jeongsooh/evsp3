from django.contrib import admin
from .models import Clients

# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
  list_display = ('cpnumber', 'cpstatus', 'channel_name_1', 'channel_status_1', 'connection_id_1', 'authorized_tag_1',
                  'channel_name_2', 'channel_status_2', 'connection_id_2', 'authorized_tag_2',)

admin.site.register(Clients, ClientsAdmin)
