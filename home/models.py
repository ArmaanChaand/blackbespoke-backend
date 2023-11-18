from django.db import models
from utils.validators import only_svg_png_images
# Create your models here.
class City(models.Model):
    icon = models.FileField(upload_to='media/images/city/', validators=[only_svg_png_images])
    name = models.CharField(max_length=50, null=False, blank=False)
    code = models.CharField(max_length=50, null=False, blank=False)

class AddressDetail(models.Model):
    address  = models.TextField(null=False, blank=False)
    landmark = models.CharField(max_length=100, null=False, blank=False)
    pin_code = models.CharField(max_length=50, null=False, blank=False)
    city     = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True, blank=True, related_name='address')
    customer = models.ForeignKey(to='user.Customer', on_delete=models.SET_NULL, null=True, blank=True, related_name='address')

