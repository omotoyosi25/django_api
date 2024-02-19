from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, exceptions
from  rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, CreateProductSerializer
from .models import Category, Product

# Create your views here.

class AddCategoryEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        category=Category.objects.all( )
        serializer=CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
       serializer= CategorySerializer(data=request.data)
       if serializer.is_valid():
           serializer.save() #calls the create or update method depends on the request 
           return Response(data=serializer.data , status=status.HTTP_201_CREATED)
       return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)
    
class ProductEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self,request,*args,**kwargs):
        serializer=CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductDetaillEndpoint(APIView):
    def get_object(self, pk):
        try:
            product=Product.objects.get(id=pk)
            return product
        except Product.DoesNotExist:
            raise exceptions.NotFound(f"product with this id {pk} does not exist")

    def get(self,request,*args,**kwargs):
        product=self.get_object(self.kwargs['product_id'])
        serializer=ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        product=self.get_object(self.kwargs['product_id'])
        serializer=CreateProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, *args, **kwargs):
        product=self.get_object(self.kwargs['product_id'])
        product.delete()
        return Response({'message':'product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)