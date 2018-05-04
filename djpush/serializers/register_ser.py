from rest_framework import serializers

from djpush.models import JiGuangReg


class RegisterCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = JiGuangReg
        exclude = ('id',)
