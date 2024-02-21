from rest_framework import serializers, exceptions
from .models import Category, Product
from django.contrib.auth.models import User



class CategorySerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50, min_length=4)
    id=serializers.IntegerField(read_only=True)



    def validate(self, attrs):
        name=attrs.get('name')
        if name == 'acid':
            raise exceptions.ValidationError('please acid is not an accepted category')
        return attrs
    

    def create(self, validated_data):
        return Category.objects.create(name=validated_data['name'])
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'name', 'description', 'price', 'dis_price', 'category', 'prod_date', 'image','exp_date', 'ratings',
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'id','name', 'description', 'price', 'dis_price', 'category', 'prod_date']
        
class UserCreateSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, max_length=68, min_length=5)
    password2=serializers.CharField(write_only=True, max_length=68, min_length=5)
    class Meta:
        model=User
        fields=[
            'username', 'email', 'password', 'password2'
        ]
    def validate(self, attrs):
        user=User.objects.filter(username=attrs.get('username'))
        if user.exists():
            raise exceptions.ValidationError('username already in use, try a different username!!')
        password1=attrs.get('password')
        password2=attrs.get("password2")
        if password1 != password2:
            raise exceptions.ValidationError("password do not match")

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])