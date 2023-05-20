from django.urls import path
from .views import (ProductListApiView,
                    ProductCreateApiView,
                    ProductDetailApiView,
                    ProductUpdateApiView,
                    ProductDestroyApiView,
                    CategoryApiView,
                    ProductFilterApiView,
                    CategoryListApiView
                    )

urlpatterns = [
    path('place_list/', ProductListApiView.as_view(), name='place_list'),
    path('place_create/', ProductCreateApiView.as_view(), name='place_create'),
    path('place_detail/<int:id>/', ProductDetailApiView.as_view(), name='place_detail'),
    path('place_update/<int:id>/', ProductUpdateApiView.as_view(), name='place_update'),
    path('place_delete/<int:id>/', ProductDestroyApiView.as_view(), name='place_delete'),
    path('filter_category/<str:name>/', CategoryApiView.as_view(), name='filter_category'),
    path('filter_place/', ProductFilterApiView.as_view(), name='filter_place'),
    path('category_list/', CategoryListApiView.as_view(), name='category_list'),
]
