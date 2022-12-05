from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from sales.models import ProductCategory
from sales.models import Product
from sales.models import Receipt
from sales.models import Sales
from sales.serializers import ProductCategorySerializer
from sales.serializers import ProductSerializer
from sales.serializers import ReceiptSerializer
from sales.serializers import SalesSerializer
from rest_framework import permissions
from sales import custompermission

class ProductCategoryList(generics.ListCreateAPIView):
	queryset = ProductCategory.objects.all()
	serializer_class = ProductCategorySerializer
	name = 'productcategory-list'

class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ProductCategory.objects.all()
	serializer_class = ProductCategorySerializer
	name = 'productcategory-detail'

class ProductList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	name = 'product-list'
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
		custompermission.IsCurrentUserOrReadOnly
	)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	name = 'product-detail'
	permission_classes=(
		permissions.IsAuthenticatedOrReadOnly,
		custompermission.IsCurrentUserOrReadOnly,
	)

class ReceiptList(generics.ListCreateAPIView):
	queryset = Receipt.objects.all()
	serializer_class = ReceiptSerializer
	name = 'receipt-list'

class ReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Receipt.objects.all()
	serializer_class = ReceiptSerializer
	name = 'receipt-detail'

class SalesList(generics.ListCreateAPIView):
	queryset = Sales.objects.all()
	serializer_class = SalesSerializer
	name = 'sales-list'

class SalesDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Sales.objects.all()
	serializer_class = SalesSerializer
	name = 'sales-detail'

class ApiRoot(generics.GenericAPIView):
	name = 'api-root'
	def get(self, request, *args, **kwargs):
		return Response({
			'product-categories' : reverse(ProductCategoryList.name, request=request), 
			'products' : reverse(ProductList.name, request=request),
			'receipts' : reverse(ReceiptList.name, request=request),
			'sales' : reverse(SalesList.name, request=request)
			})