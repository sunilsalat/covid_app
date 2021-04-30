from django.contrib import admin
from .models import User_custom, Hospital, Tiffin_service_provider

# Register your models here.

admin.site.register(User_custom)
admin.site.register(Hospital)
admin.site.register(Tiffin_service_provider)
