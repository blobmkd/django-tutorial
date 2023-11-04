from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin

class ProductListCreateAPIView(
    generics.ListCreateAPIView,
    StaffEditorPermissionMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)

class ProductDetailAPIView(
    generics.RetrieveAPIView,
    StaffEditorPermissionMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIView(
    generics.ListAPIView,
    StaffEditorPermissionMixin
    ):
    """
    Not gonna use this one, we are changing the above ProductCreateAPIView
    to ProductListCreateAPIView.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(
    generics.UpdateAPIView,
    StaffEditorPermissionMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyAPIView(
    generics.DestroyAPIView,
    StaffEditorPermissionMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)