from django.contrib import admin
from .models import Employee, Store, Visit


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']
    search_fields = ['name']


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class VisitAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'store', 'latitude', 'longitude']
    search_fields = ['employee__name', 'store__name']


admin.site.register(Employee)
admin.site.register(Store)
admin.site.register(Visit)
