from rest_framework import serializers
from .models import ShopModel


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = ('__all__')