from django.urls import path
from .views import CommentsViewSet, PlaceRatingAPIView

urlpatterns = [
    path('comments/', CommentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments-list'),
    path('comments/<int:pk>/', CommentsViewSet.as_view({'get': 'retrieve'}), name='comments-detail'),
    path('plane_rating/', PlaceRatingAPIView.as_view(), name='place_rating'),
]
