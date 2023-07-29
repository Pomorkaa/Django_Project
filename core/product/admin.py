from django.contrib import admin
from .models import Status, Trip, Trip_type ,  AdditionalImage , AdditionalOptions
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.db import models

class CustomAdminFileWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        result = []
        if value:
            if hasattr(value, "url"):
                result.append(
                    f'''<a href="{value.url}" target="_blank">
                        <img 
                            src="{value.url}" alt="{value}" 
                            width="100" height="100"
                            style="object-fit: cover;"
                        />
                        </a>'''
                )
        result.append(super().render(name, value, attrs, renderer))
        return format_html("".join(result))




class AdditionalImageInline(admin.StackedInline):
    model = AdditionalImage
    extra = 0
    formfield_overrides = {models.ImageField: {"widget": CustomAdminFileWidget}} 



class TripAdmin(admin.ModelAdmin):
    list_display = ('company','name', 'type', 
                     'seets', 'children_seets','disabled_seets','time','status')
    list_editable = ('status',)
    list_filter = ('company', 'name', 'type','status')
    search_fields = ('company', 'name', 'type','status')
    sortable_by = ['company', 'type', 
                     'seets', 'children_seets','disabled_seets','status']
    list_per_page = 20
    inlines = [
        AdditionalImageInline,
    ]



class StatusTripAdmin(admin.ModelAdmin):
    list_display = ('status',)
    list_per_page = 20

class TripInline(admin.StackedInline):
    model = Trip
    extra = 1
    
    
class AdditionalOptionsModelAdmin(admin.ModelAdmin):
    list_display = ("option",)


admin.site.register(Trip,TripAdmin)
admin.site.register(Status, StatusTripAdmin)
admin.site.register(Trip_type)
admin.site.register(AdditionalOptions, AdditionalOptionsModelAdmin)