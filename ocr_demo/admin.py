from django.contrib import admin
from ocr_demo.models import NetworkData
# Register your models here.

class NetworkAdmin(admin.ModelAdmin):
    list_display = ("method_name", "category_one", "category_two", "category_three", "category_four")
admin.site.register(NetworkData, NetworkAdmin)
