from django.urls import path
from .views import (TransportListApiView,
                    TransportCreateApiView, TransportSearchApiView,
                    TransportUpdateApiView,
                    TransportDestroyApiView,
                    TransportDetailApiView)

urlpatterns = [
    path('list/', TransportListApiView.as_view(), name='transport_list'),
    path('create/', TransportCreateApiView.as_view(), name='transport_create'),
    path('update/<int:id>/', TransportUpdateApiView.as_view(), name='transport_update'),
    path('delete/<int:id>/', TransportDestroyApiView.as_view(), name='transport_delete'),
    path('detail/<int:id>/', TransportDetailApiView.as_view(), name='transport_detail'),
    path('search/', TransportSearchApiView.as_view(), name='transport_search'),
]
