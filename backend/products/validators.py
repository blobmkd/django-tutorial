from rest_framework import serializers

from .models import Product

def validate_title(value):
        qs = Product.objects.filter(title__iexact = value) # checks if the title that we are passing in exists on our project somewhere
        # iexact - means case insensitive search per queryset
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value