from django.contrib.auth.models import User, Group
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    permission = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'permission')
        extra_kwargs = {'password': {'write_only': True}}





    def validate(self, data):

        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')

        permission = validated_data.pop('permission')

        validated_data['is_active'] = False

        user = User.objects.create_user(**validated_data)

        user_group, created = Group.objects.get_or_create(name=permission)
        user.groups.add(user_group)

        return user
