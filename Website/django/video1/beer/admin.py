from django.contrib import admin
from beer.models import Beer, Brewery
# Register your models here.

class BeerAdmin(admin.ModelAdmin):
    prepopulated_fields = [ ('slug' , 'name')]


admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery)