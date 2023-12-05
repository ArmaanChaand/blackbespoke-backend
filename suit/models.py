from django.db import models
from utils.validators import only_svg_png_images
# Create your models here.
class PriceNDescriptions(models.Model):
    class currencies(models.TextChoices):
        CHOICE_ONE = 'INR', 'INR'
        CHOICE_TWO = 'USD', 'USD'
        
    currency = models.CharField(
        max_length=20,
        choices=currencies.choices,
        default=currencies.CHOICE_ONE
    )
    price       = models.DecimalField(decimal_places=2, max_digits=9, null=True, blank=True)
    composition = models.CharField(max_length=100, null=True, blank=True)
    season      = models.CharField(max_length=100, null=True, blank=True)
    fitness     = models.CharField(max_length=100, null=True, blank=True)
    weight      = models.CharField(max_length=100, null=True, blank=True)

class Fabric(PriceNDescriptions):
    name = models.CharField(max_length=150, null=True, blank=True)
    picture = models.ImageField(upload_to='images/suit/')

class BlazerPattern(PriceNDescriptions):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icon = models.FileField(upload_to='images/city/', validators=[only_svg_png_images])
    picture = models.ImageField(upload_to='images/suit/')

class WaistcoatPattern(BlazerPattern):
    pass
class WaistcoatLapel(BlazerPattern):
    pass
class PantStyle(BlazerPattern):
    pass
class ShirtColor(PriceNDescriptions):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icon = models.FileField(upload_to='images/city/', validators=[only_svg_png_images])


class SuitBuild(models.Model):
    monogram_text     = models.CharField(max_length=150, null=True, blank=True)
    fabric            = models.OneToOneField(to=Fabric, on_delete=models.SET_NULL, null=True, blank=True, related_name='fabric_suit')
    blazer_pattern    = models.OneToOneField(to=BlazerPattern, on_delete=models.SET_NULL, null=True, blank=True, related_name='blazer_suit')
    waistcoat_pattern = models.OneToOneField(to=WaistcoatPattern, on_delete=models.SET_NULL, null=True, blank=True, related_name='waistcoat_pattern_suit')
    waistcoat_lapel   = models.OneToOneField(to=WaistcoatLapel, on_delete=models.SET_NULL, null=True, blank=True, related_name='waistcoat_lapel_suit')
    pant_style        = models.OneToOneField(to=PantStyle, on_delete=models.SET_NULL, null=True, blank=True, related_name='pant_style_suit')
    shirt_color       = models.OneToOneField(to=ShirtColor, on_delete=models.SET_NULL, null=True, blank=True, related_name='shirt_color_suit')