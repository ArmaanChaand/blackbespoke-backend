from django.db import models
from utils.validators import only_svg_png_images
# Create your models here.

class SuitPartDetail(models.Model):
    is_active   = models.BooleanField(default=True)
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
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.description}"

class Fabric(models.Model):
    is_active   = models.BooleanField(default=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    icon = models.ImageField(upload_to='images/suit/', null=True, blank=True)
    pictures = models.ManyToManyField(to='home.Pictures', related_name='fabric_pics', blank=True)
    detail = models.ForeignKey(to=SuitPartDetail, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class BlazerPattern(models.Model):
    is_active   = models.BooleanField(default=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icon = models.FileField(upload_to='images/suit/', validators=[only_svg_png_images])
    pictures = models.ManyToManyField(to='home.Pictures', related_name='its_pics', blank=True)
    detail = models.ForeignKey(to=SuitPartDetail, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    

class WaistcoatPattern(BlazerPattern):
    pass
class WaistcoatLapel(BlazerPattern):
    pass
class PantStyle(BlazerPattern):
    pass
class ShirtColor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    icon = models.ImageField(upload_to='images/suit/', null=True, blank=True)
    pictures = models.ManyToManyField(to='home.Pictures', related_name='shirt_pics', blank=True)
    detail = models.ForeignKey(to=SuitPartDetail, on_delete=models.SET_NULL, null=True, blank=True)
    


class SuitBuild(models.Model):
    is_active         = models.BooleanField(default=True)
    monogram_text     = models.CharField(max_length=150, null=True, blank=True)
    fabric            = models.ForeignKey(to=Fabric, on_delete=models.SET_NULL, null=True, blank=True, related_name='fabric_suit')
    blazer_pattern    = models.ForeignKey(to=BlazerPattern, on_delete=models.SET_NULL, null=True, blank=True, related_name='blazer_suit')
    waistcoat_pattern = models.ForeignKey(to=WaistcoatPattern, on_delete=models.SET_NULL, null=True, blank=True, related_name='waistcoat_pattern_suit')
    waistcoat_lapel   = models.ForeignKey(to=WaistcoatLapel, on_delete=models.SET_NULL, null=True, blank=True, related_name='waistcoat_lapel_suit')
    pant_style        = models.ForeignKey(to=PantStyle, on_delete=models.SET_NULL, null=True, blank=True, related_name='pant_style_suit')
    shirt_color       = models.ForeignKey(to=ShirtColor, on_delete=models.SET_NULL, null=True, blank=True, related_name='shirt_color_suit')

    