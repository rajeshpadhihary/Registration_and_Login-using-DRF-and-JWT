from rest_framework import serializers
from .models import customUser
from django.contrib.auth.hashers import check_password

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 70,min_length = 6, write_only = True)
    password2 = serializers.CharField(max_length = 70,min_length = 6, write_only = True)

    class Meta:
        model = customUser
        fields = ['email','username','first_name','last_name','password','password2']

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password2']
        if password != password2:
                raise serializers.ValidationError({'error': 'Password must match with confirm password.'})
        return attrs
    
    def create(self, validated_data):
        email=validated_data.get('email')
        username = validated_data.get('username')
        first_name=validated_data.get('first_name')
        last_name=validated_data.get('last_name')
        password=validated_data['password']
        

        user = customUser.creation.create_user(email = email,username = username,first_name = first_name,last_name = last_name,password = password)
        
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length = 70)
    password = serializers.CharField(max_length = 100)

    class Meta:
        model = customUser
        fields = ['email','password']
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user_obj = customUser.creation.all()

        for i in user_obj:
            if i.email == email:
                if check_password(password,i.password) == True:
                    return attrs
                else:
                    raise serializers.ValidationError('Password is Incorrect')  
            if check_password(password,i.password) == True:
                if i.email ==email:
                    return attrs
                else:
                    raise serializers.ValidationError({'error': 'Please Check Your Email'})
        raise serializers.ValidationError({'error': 'Please Register First'})
            
