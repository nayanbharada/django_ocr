from rest_framework import serializers
from ocr_demo.models import NetworkData


class NetworkDataSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Class container containing information of the model.
        """
        model = NetworkData
        fields = '__all__'