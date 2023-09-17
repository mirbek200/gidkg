from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.transport.models import Transport
from apps.transport.serializers import TransportSerializer
from apps.users.permissions import IsOwnerOrReadOnly

from django.db.models import Q

class TransportSearchApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        query = request.data.get('query', None)
        if query is not None:
            transports = Transport.objects.filter(Q(where_from__icontains=query) | Q(where_to__icontains=query))
            serializers = TransportSerializer(transports, many=True)
            return Response(serializers.data)
        return Response({"error": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)

class TransportCreateApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransportSerializer

    def post(self, request):
        serializers = TransportSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportListApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        category = Transport.objects.all()
        serializers = TransportSerializer(category, many=True)
        return Response(serializers.data)


class TransportDetailApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Transport.objects.get(id=id)
        except Transport.DoesNotExist:
            raise Http404

    def get(self, request, id):
        transport = self.get_object(id)
        serializers = TransportSerializer(transport)
        data = serializers.data
        return Response(data)


class TransportUpdateApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TransportSerializer

    def get_object(self, id):
        try:
            return Transport.objects.get(id=id)
        except Transport.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        transport = self.get_object(id)
        serializer = TransportSerializer(transport, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportDestroyApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, id):
        try:
            return Transport.objects.get(id=id)
        except Transport.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        transport = self.get_object(id)
        transport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
