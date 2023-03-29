from django.contrib import admin
from  abcon.models import about_fun 
# Register your models here.
class abcon_admin(admin.ModelAdmin):
    list_display=('title','contant')
admin.site.register(about_fun,abcon_admin)