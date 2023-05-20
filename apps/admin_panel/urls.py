from django.urls import path
from .views import (CategoryCreateApiView,
                    CategoryUpdateApiView,
                    CategoryDeleteApiView
                    )

urlpatterns = [
    path('category_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('category_update/<int:id>/', CategoryUpdateApiView.as_view(), name='cat_update'),
    path('category_delete/<int:id>/', CategoryDeleteApiView.as_view(), name='cat_delete'),
]
