from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Guest, Room, Booking
from .serializers import GuestSerializer, RoomSerializer, BookingSerializer

class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]
    queryset = Guest.objects.all()  # Добавили обратно

    def get_queryset(self):
        # Переопределяем, чтобы пользователь видел только себя
        return Guest.objects.filter(id=self.request.user.id)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()  # Добавили обратно

    def get_queryset(self):
        return Booking.objects.filter(guest=self.request.user)

    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)