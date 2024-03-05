from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, exceptions, generics, permissions
from  rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import CategorySerializer, ProductSerializer, CreateProductSerializer, UserCreateSerializer
from .models import Category, Product 

# Create your views here.

# class AddCategoryEndpoint(APIView):
#     def get(self, request, *args, **kwargs):
#         category=Category.objects.all( )
#         serializer=CategorySerializer(category, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):
#         request.data
#         serializer=CategorySerializer(data=request.data)
#         if serializer.is_valid():#calls the validate method in our serializer
#             serializer.save()#calls the create(post) or update(put) method depending on the request type
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def post(self, request, *args, **kwargs):
    #    serializer= CategorySerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save() #calls the create or update method depends on the request 
    #        return Response(data=serializer.data, status=status.HTTP_201_CREATED) 
    #    return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

class UpgradedCategoryEndpoint(generics.ListCreateAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer

class SingleCategoryEndpoint(generics.RetrieveAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'

class CategoryDeleteEndpoint(generics.DestroyAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'
    
# class ProductEndpoint(APIView):
#     def get(self, request, *args, **kwargs):
#         products=Product.objects.all()
#         serializer=ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def post(self,request,*args,**kwargs):
#         serializer=CreateProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateProductEndpoint(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class=CreateProductSerializer

class SingleProductEndpoint(generics.RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class=CreateProductSerializer
    lookup_field='pk'

class ProductDeleteEndpoint(generics.DestroyAPIView):
    queryset= Product.objects.all()
    serializer_class=CreateProductSerializer
    lookup_field='pk' 
    
class ProductListEndpoint(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def get_queryset(self):
        queryset=super().get_queryset()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset=queryset.filter(category__name=category)
        return queryset
    

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
    

# class UserRegistrationEndpoint(generics.CreateAPIView):
#     queryset=User.objects.all()
#     permission_classes=[permissions.AllowAny]
#     serializer_class=UserCreateSerializer