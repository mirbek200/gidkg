from django.urls import path
from .views import (CategoryCreateApiView,
                    CategoryUpdateApiView,
                    CategoryDeleteApiView,
                    PlaceUpdateApiView,
                    PlaceDestroyApiView,
                    AddManagerApiView
                    )

urlpatterns = [
    path('category_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('category_update/<int:id>/', CategoryUpdateApiView.as_view(), name='cat_update'),
    path('category_delete/<int:id>/', CategoryDeleteApiView.as_view(), name='cat_delete'),

    path('place_update/<int:id>/', PlaceUpdateApiView.as_view(), name='cat_update'),
    path('place_delete/<int:id>/', PlaceDestroyApiView.as_view(), name='cat_delete'),

    path('add_manager/', AddManagerApiView.as_view(), name='add_manager'),
]
