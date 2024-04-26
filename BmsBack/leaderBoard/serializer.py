from rest_framework import serializers
from .models import LeaderBoardMember



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoardMember
        fields = ['playerId', 'phoneNumber', 'numberOfConsumedLives', 'playerLastLevel', 'playTime']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        phone_number = representation.get('phoneNumber', '')
        if len(phone_number) > 4:
            start = phone_number[:len(phone_number)//2 - 1]
            end = phone_number[len(phone_number)//2 + 2:]
            representation['phoneNumber'] = start + '***' + end
        return representation