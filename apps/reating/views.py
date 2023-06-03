from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CommentSerializer, RatingSerializer
from .models import Comment


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

comments_viewset = CommentsViewSet.as_view({'get': 'list', 'post': 'create'})


class PlaceRatingAPIView(APIView):
    serializer_class = RatingSerializer

    def post(self, request):
        serializers = RatingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
