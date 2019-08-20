# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from app01.models import Customer
from app01.resource import CustomerResource


@admin.register(Customer)
class CusModelAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin):
    resource_class = CustomerResource
    list_display = ('id', 'name', 'phone', 'type', 'company_code', 'time_create', 'time_update')
    list_filter = ('phone', 'name','time_create')
