from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from django.contrib.auth.models import Group
from .models import Registration, contact, Life_Insurance, Health_Insurance, Motor_Insurance, Campaign, Form_Campaign, Capping, APKEducation, SecureCare, Fire_Insurance, Marine_Insurance, Liability_Insurance, A_H_Insurance, Credit_Card, Credit_Card_Bank, complaint, Credit_Card_Banking

admin.site.site_header = 'APK WEB AGGREGATOR'


class registration(ImportExportModelAdmin):
    list_display = ('sno', 'name', 'email', 'phone', 'Pending_Points', 'Points', 'date')


class Contact(admin.ModelAdmin):
    list_display = ('sno', 'first_name', 'last_name', 'email', 'subject', 'message', 'date')


class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('sno', 'First_Name', 'Last_Name', 'Email', 'Mobile', 'date')


class Insuranceadmin(admin.ModelAdmin):
    list_display = ('sno', 'Vehicle_Name', 'Vehicle_Registration_No', 'Policy_Issue_Date', 'premium_Paid', 'date')


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('Active', 'sno', 'Campaign_Name', 'points', 'Capping', 'Validity', 'date')


class Form_campaign(admin.ModelAdmin):
    list_display = ('sno', 'User_Email', 'Send_on', 'Conformed', 'date')


class capping(admin.ModelAdmin):
    list_display = ('Conformed', 'sno', 'Campaign_Name', 'User_Email', 'Pending_Points', 'Points', 'date')


class secure(admin.ModelAdmin):
    list_display = ('Verified', 'sno', 'First_Name', 'Last_Name', 'Mobile', 'Email', 'date')


class apkeducation(admin.ModelAdmin):
    list_display = ('Verified', 'sno', 'First_Name', 'Last_Name', 'Mobile', 'Email', 'date')


class other_insurance(admin.ModelAdmin):
    list_display = ('Name', 'Mobile', 'Organization_Name', 'Email', 'date')

class Creditcard_bank(admin.ModelAdmin):
    list_display = ('Active', 'Bank_Name', 'All_Pin_Code', 'Document')

class Creditcard(admin.ModelAdmin):
    list_display = ('sno', 'Status', 'Customer_Name', 'Contact', 'Customer_Email', 'Action', 'date')


class Complaint(ImportExportModelAdmin):
    list_display = ('sno', 'Name', 'User_ID', 'phone', 'subject', 'message', 'date')


class creditCardBank(ImportExportModelAdmin):
    list_display = ('sno','Active', 'Bank_Name', 'date')


admin.site.register(Registration, registration)
admin.site.register(contact, Contact)
admin.site.register(Life_Insurance, InsuranceAdmin)
admin.site.register(Health_Insurance, InsuranceAdmin)
admin.site.register(Motor_Insurance, Insuranceadmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Form_Campaign, Form_campaign)
admin.site.register(Capping, capping)
admin.site.register(APKEducation, apkeducation)
admin.site.register(SecureCare, secure)
admin.site.register(Fire_Insurance, other_insurance)
admin.site.register(Marine_Insurance, other_insurance)
admin.site.register(Liability_Insurance, other_insurance)
admin.site.register(A_H_Insurance, other_insurance)
admin.site.register(Credit_Card, Creditcard)
admin.site.register(Credit_Card_Bank, Creditcard_bank)
admin.site.register(complaint, Complaint)
admin.site.register(Credit_Card_Banking, creditCardBank)
