from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.place.models import Place, Category
from apps.place.serializers import PlaceSerializer, CategorySerializer
from rest_framework import permissions, status, generics
from django.core.paginator import Paginator
from apps.users.permissions import IsOwnerOrReadOnly


class PlaceListApiView(APIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get(self,  request):
        places = Place.objects.all()
        paginator = Paginator(places, 5)
        page_num = self.request.query_params.get('page')
        serializers = PlaceSerializer(paginator.page(page_num), many=True)
        return Response(serializers.data)


class PlaceFilterApiView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class PlaceCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlaceSerializer

    def post(self, request):
        serializers = PlaceSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaceDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Place.objects.get(id=id)
        except Place.DoesNotExist:
            raise Http404

    def get(self, request, id):
        place = self.get_object(id)
        serializers = PlaceSerializer(place)
        data = serializers.data
        return Response(data)


class PlaceUpdateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
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
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, id):
        try:
            return Place.objects.get(id=id)
        except Place.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        place = self.get_object(id)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListApiView(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)


class CategoryApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, name):
        category = self.get_object(name)
        place = Place.objects.filter(category_id__name=name)
        serializer = CategorySerializer(category)
        serializer2 = PlaceSerializer(place, many=True)
        data = serializer.data
        data['place'] = serializer2.data
        return Response(data)
