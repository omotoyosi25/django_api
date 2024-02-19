from rest_framework import serializers, exceptions
from .models import Category, Product



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
            'id','name', 'description', 'price', 'dis_price', 'category'
        ]