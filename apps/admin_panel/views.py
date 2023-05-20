from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.place.models import Category
from apps.place.serializers import CategorySerializer


class CategoryCreateApiView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateApiView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        category = self.get_object(id)
        serializer = CategorySerializer(category, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteApiView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
