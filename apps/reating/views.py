from django.db.models import Avg
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CommentSerializer, RatingSerializer
from .models import Comment, Rating
from ..place.models import Place
from ..users import permissions
from ..users.permissions import IsOwnerOrReadOnly


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

comments_viewset = CommentsViewSet.as_view({'get': 'list', 'post': 'create'})


class CreatePlaceRatingAPIView(APIView):
    serializer_class = RatingSerializer

    def post(self, request):
        serializers = RatingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailPlaceRatingView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer

    def get_rating_object(self, rating_id):
        try:
            rating = Rating.objects.get(id=rating_id)
            return rating
        except Rating.DoesNotExist:
            return None

    def put(self, request, rating_id):
        rating = self.get_rating_object(rating_id)
        if not rating:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rating_id):
        rating = self.get_rating_object(rating_id)
        if not rating:
            return Response(status=status.HTTP_404_NOT_FOUND)

        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlaceRatingAPIView(APIView):
    def get(self, request):
        ratings = Rating.objects.values('place_id').annotate(avg_rating=Avg('number'))

        result = {}
        for rating in ratings:
            place_id = rating['place_id']
            avg_rating = rating['avg_rating']
            result[place_id] = avg_rating

        return Response(result)

