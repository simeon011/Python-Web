from django.contrib.auth import get_user_model
from django.db.models import Count, Min, Max
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from garage.models import Car, Manufacturer, Part
from garage.serialixers import CarSerializer, ManufacturerSerializer, PartSerializer, \
    ManufacturerNestedReadSerializer, CarNestedReadSerializer, PartWriteSerializer


class ReadWriteSerializerMixin:
    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.read_serializer_class
        return ManufacturerSerializer


class ListCreateCar(ReadWriteSerializerMixin, ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.select_related('manufacturer').prefetch_related('parts').all()
    read_serializer_class = CarNestedReadSerializer
    write_serializer_class = CarSerializer


class CarStatsView(APIView):
    def get(self, request):
        stats = Car.objects.aggregate(
            total_cars=Count('id'),
            oldest_year=Min('year'),
            newest_year=Max('year'),
        )
        return Response(stats, status=status.HTTP_200_OK)


class RetrieveUpdateDestroyCarAPIView(ReadWriteSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.select_related('manufacturer').prefetch_related('parts').all()
    read_serializer_class = CarNestedReadSerializer
    write_serializer_class = CarSerializer


class ListCreateManufacturerAPIView(ListCreateAPIView, ReadWriteSerializerMixin):
    queryset = Manufacturer.objects.prefetch_related('cars', 'parts').all()
    read_serializer = ManufacturerNestedReadSerializer
    write_serializer = ManufacturerSerializer


class PartModelViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Part.objects.all()
    read_serializer = PartSerializer
    write_serializer = PartWriteSerializer


class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        User = get_user_model()
        data = {
            'users_count': User.objects.count(),
            'manufacturers_count': User.objects.count(),
            'cars_count': Car.objects.count(),
            'parts_count': Part.objects.count(),
            'requested_by': request.user.username,
        }
        return Response(data=data, status=status.HTTP_200_OK)