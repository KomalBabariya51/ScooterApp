from rest_framework import serializers
from .models import ScooterAvailability, ScooterLogs

#
# class ScooterDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScooterDetails
#         fields = '__all__'


class ScooterAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScooterAvailability
        fields = ["id", "scooter_lati", "scooter_long", "scooter_status"]


class ScooterLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScooterLogs
        fields = "__all__"
