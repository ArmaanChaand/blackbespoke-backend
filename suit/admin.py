from django.contrib import admin
from .models import SuitBuild, Fabric, BlazerPattern, WaistcoatPattern,WaistcoatLapel, PantStyle, ShirtColor, PartDetail
# Register your models here.
admin.site.register(PartDetail)
admin.site.register(Fabric)
admin.site.register(BlazerPattern)
admin.site.register(WaistcoatPattern)
admin.site.register(WaistcoatLapel)
admin.site.register(PantStyle)
admin.site.register(ShirtColor)
admin.site.register(SuitBuild)