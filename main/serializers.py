from rest_framework.serializers import ModelSerializer # type: ignore

from .models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    
    