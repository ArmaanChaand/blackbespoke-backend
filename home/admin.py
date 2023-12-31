from django.contrib import admin
from .models import City, AddressDetail, Pictures, Testimonials
# Register your models here.
admin.site.register(City)
admin.site.register(AddressDetail)
admin.site.register(Pictures)
admin.site.register(Testimonials)