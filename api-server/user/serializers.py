
from rest_framework import serializers  
from user.models import User

class UserSerializer(serializers.ModelSerializer): 

    class Meta:
        model = User
        fields = ('oauth', 'email')


    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.oauth = validated_data.get('oauth', instance.pw)
        instance.email = validated_data.get('email', instance.content)
        instance.save()
        return instance
