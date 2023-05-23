from rest_framework import serializers

from apps.users.models import MyUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'name', 'email', 'phone_number', 'password']
