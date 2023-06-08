from django.urls import path
from .views import (CommentsViewSet, CreatePlaceRatingAPIView, PlaceRatingAPIView,
                    DetailPlaceRatingView)

urlpatterns = [
    path('comments/', CommentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments-list'),
    path('comments/<int:pk>/', CommentsViewSet.as_view({'get': 'retrieve'}), name='comments-detail'),
    path('create_rating/', CreatePlaceRatingAPIView.as_view(), name='create_rating'),
    path('place_rating/', PlaceRatingAPIView.as_view(), name='place_rating'),
    path('detail_ratings/<int:rating_id>/', DetailPlaceRatingView.as_view(), name='rating-detail'),
]
