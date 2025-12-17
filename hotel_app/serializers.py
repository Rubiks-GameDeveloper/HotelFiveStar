from rest_framework import serializers
from .models import Guest, Room, Booking

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'username', 'email', 'phone_number', 'address']
        read_only_fields = ['id']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    guest_id = serializers.PrimaryKeyRelatedField(
        queryset=Guest.objects.all(), source='guest', write_only=True
    )
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True
    )

    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        # Автоматически привязываем к текущему пользователю, если не указан
        if 'guest' not in validated_data:
            validated_data['guest'] = self.context['request'].user
        return super().create(validated_data)