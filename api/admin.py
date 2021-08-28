from django.contrib import admin
from .models import Plant,Owner,Message
# Register your models here.

admin.site.register(Plant)
admin.site.register(Owner)
admin.site.register(Message)