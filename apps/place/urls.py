from django.urls import path
from .views import *

urlpatterns = [
    path('place_list/', PlaceListApiView.as_view(), name='place_list'),
    path('place_create/', PlaceCreateApiView.as_view(), name='place_create'),
    path('place_detail/<int:id>/', PlaceDetailApiView.as_view(), name='place_detail'),
    path('place_update/<int:id>/', PlaceUpdateApiView.as_view(), name='place_update'),
    path('place_delete/<int:id>/', PlaceDestroyApiView.as_view(), name='place_delete'),
    path('filter_category/<str:name>/', CategoryApiView.as_view(), name='filter_category'),
    path('filter_place/', PlaceFilterApiView.as_view(), name='filter_place'),
    path('category_list/', CategoryListApiView.as_view(), name='category_list'),
]
