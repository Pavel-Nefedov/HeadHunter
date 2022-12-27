from django.contrib import admin

from companyapp.models import Company, CompanyProfile, Vacancy

admin.site.register(Company)
admin.site.register(CompanyProfile)
admin.site.register(Vacancy)
