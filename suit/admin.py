from django.contrib import admin
from .models import SuitBuild, Fabric
# Register your models here.
admin.site.register(Fabric)
admin.site.register(SuitBuild)