# Register your models here.
from app01.models import Customer
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'type', 'company_code', 'time_create')


@admin.register(Customer)
class CusModelAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin):
    resource_class = CustomerResource
    list_display = ('id', 'name', 'phone', 'type', 'company_code', 'time_create', 'time_update')
    list_filter = ('phone', 'name', 'time_create')
