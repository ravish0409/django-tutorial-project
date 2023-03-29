from django.contrib import admin
from  service.models import service 
# Register your models here.
class serv_admin(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(service,serv_admin)