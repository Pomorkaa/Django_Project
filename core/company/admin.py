from django.contrib import admin
from .models import Company , Manager, Document , Contacts
from product.admin import TripInline
# Register your models here.



class Company_Admin(admin.ModelAdmin):
    model = Company
    list_display =('name','manager','phone','referal', 'requisites')
    inlines = (TripInline,)



admin.site.register(Company, Company_Admin)
admin.site.register(Manager)
admin.site.register(Document)
admin.site.register(Contacts)




