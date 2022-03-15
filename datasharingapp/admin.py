from django.contrib import admin

from datasharingapp.models import Owner, Receiver, Upload, Download

admin.site.register(Owner)
admin.site.register(Receiver)
admin.site.register(Upload)
admin.site.register(Download)
