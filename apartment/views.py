from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework import generics 
from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from .models import ApartmentModel, MyRentsModel
from .serializer import AparmentSerializer, MyRentSerializer
from .filters import RoomFilter

User = get_user_model()

#views для списка орендованных домов пользавателя
class MyRentList(generics.ListAPIView):
    queryset = MyRentsModel.objects.all()
    serializer_class = MyRentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_classes = [RoomFilter]

class MyRentRetrieve(generics.RetrieveAPIView):
    queryset = MyRentsModel.objects.all()
    serializer_class = MyRentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'pk'

class MyRentCreate(generics.CreateAPIView):
    queryset = MyRentsModel.objects.all()
    serializer_class = MyRentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    apart = ApartmentModel.objects.all()
    apart.active = True


class MyRentDelete(generics.DestroyAPIView):
    queryset = MyRentsModel.objects.all
    serializer_class = MyRentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    apart = ApartmentModel.objects.all()
    apart.active = False
    lookup_field = 'pk'


#views  для всех домов/квартир на сайте
class ApartMentList(generics.ListAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = AparmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter




class ApartMentRetrieve(generics.RetrieveAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = AparmentSerializer
    lookup_field = 'pk'



 