from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Country)
admin.site.register(Color)
admin.site.register(Manufacturer)

admin.site.register(TVPhoto)
admin.site.register(TV)
admin.site.register(TVOS)
admin.site.register(TVresolution)
admin.site.register(TVOuts)

admin.site.register(WM)
admin.site.register(WMPhoto)

admin.site.register(Fridge)
admin.site.register(FridgePhoto)

admin.site.register(Oven)
admin.site.register(OvenPhoto)

admin.site.register(DryMashine)
admin.site.register(DryPhoto)

admin.site.register(Vacum)
admin.site.register(VacumCleanerPhoto)

admin.site.register(Microwave)
admin.site.register(MicrowavePhoto)

admin.site.register(Cooker)
admin.site.register(CookerPhoto)

admin.site.register(DishWasher)
admin.site.register(DishWasherPhoto)


