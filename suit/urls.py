from django.urls import path
from .views import (
      read_fabric_all, read_blazer_pattern_all,read_waistcoat_pattern_all, 
      read_waistcoat_lapel_all, read_pant_style_all, read_shirt_color_all,read_suit_part_detail_one,
      read_suit_build_one, read_suit_build_all, create_suit_build, update_suit_build
      )

urlpatterns = [
   path('all/', read_suit_build_all, name='suit-build-all'),
   path('one/<str:suit_id>/', read_suit_build_one, name='suit-build-one'),
   path('create/', create_suit_build, name='suit-build-create'),
   path('update/<str:suit_id>/', update_suit_build, name='suit-build-one'),
   path('fabric/all/', read_fabric_all, name='fabric-all'),
   path('blazer-pattern/all/', read_blazer_pattern_all, name='blazer-pattern-all'),
   path('waistcoat-pattern/all/', read_waistcoat_pattern_all, name='waistcoat-pattern-all'),
   path('waistcoat-lapel/all/', read_waistcoat_lapel_all, name='waistcoat-lapel-all'),
   path('pant-style/all/', read_pant_style_all, name='pant-style-all'),
   path('shirt-color/all/', read_shirt_color_all, name='shirt-color-all'),
   path('shirt-color/all/', read_shirt_color_all, name='shirt-color-all'),
   path('suit-part/<str:detail_id>/', read_suit_part_detail_one, name='shirt-color-all'),
]