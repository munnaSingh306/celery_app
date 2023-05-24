from rest_framework import serializers

from model_app.models import FirstModel
from model_app.validators import password_validator


class FirstModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2, max_length=200)
    title = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    email = serializers.EmailField()
    profile_pic = serializers.ImageField(upload_to='images/userProfile/', allow_null=True, allow_blank=True)
    password = serializers.CharField(max_length=20, validators=[password_validator])

    class Meta:
        model = FirstModel
        fields = '__all__'
