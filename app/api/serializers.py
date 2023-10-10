from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from app.models import Notes, User
# from django.contrib.auth.models import User


class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields ='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']

