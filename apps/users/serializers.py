from django.forms import ValidationError, fields_for_model
from rest_framework import serializers, pagination
from .models import CustomUser



class UserSerializerCustom(serializers.Serializer):
    birthdate = serializers.DateField()
    username = serializers.CharField(max_length=255, allow_blank=True)
    email = serializers.CharField(max_length=255)
    is_staff = serializers.BooleanField()
    #validacion individual
    def validate_username(self, value):
        # I can acces to another fields with 
        # self.context
        if value == '':
            raise serializers.ValidationError('username cant be blank')
        return value
    #validacion general
    def validate(self, data):
        return data

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        exclude = ('date_joined', 'last_login')
    def create(seld, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = ('username', 'email')