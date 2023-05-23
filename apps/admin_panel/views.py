from django.http import Http404
from rest_framework import status, permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.place.models import Category, Place
from apps.place.serializers import CategorySerializer, PlaceSerializer
from apps.users.models import MyUser
from apps.admin_panel.serializers import UserSerializer
from apps.users.permissions import IsManager


class CategoryCreateApiView(APIView):
    permission_classes = [IsManager]
    serializer_class = CategorySerializer

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateApiView(APIView):
    permission_classes = [IsManager]
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
    permission_classes = [IsManager]
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


class PlaceUpdateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsManager]
    serializer_class = PlaceSerializer

    def get_object(self, id):
        try:
            return Place.objects.get(id=id)
        except Place.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        place = self.get_object(id)
        serializer = PlaceSerializer(place, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaceDestroyApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsManager]

    def get_object(self, id):
        try:
            return Place.objects.get(id=id)
        except Place.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        place = self.get_object(id)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddManagerApiView(APIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            user = MyUser.objects.create(
                email=request.data['email'],
                phone_number=request.data['phone_number'],
                is_manager=True
            )
            user.set_password(request.data['password'])
            user.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


