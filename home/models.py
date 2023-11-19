from django.db import models
from utils.validators import only_svg_png_images
# Create your models here.
class City(models.Model):
    is_active = models.BooleanField(default=True)
    icon = models.FileField(upload_to='media/images/city/', validators=[only_svg_png_images])
    name = models.CharField(max_length=50, null=False, blank=False)
    code = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return self.code

class AddressDetail(models.Model):
    is_active = models.BooleanField(default=True)
    address  = models.TextField(null=True, blank=True, default='TBA')
    landmark = models.CharField(max_length=100, null=True, blank=True, default='TBA')
    pin_code = models.CharField(max_length=50, null=True, blank=True, default='TBA')
    city     = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True, blank=True, related_name='address')
    customer = models.ForeignKey(to='user.Customer', on_delete=models.SET_NULL, null=True, blank=True, related_name='address')

    def __str__(self) -> str:
        return f"{self.address[:10]} • {self.customer} • {self.city}" 

