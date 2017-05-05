from django.contrib import admin

# Register your models here.
from company.models import CompanyModel


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(CompanyModel,CompanyAdmin)



