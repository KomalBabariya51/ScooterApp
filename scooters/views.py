from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .serializers import ScooterAvailabilitySerializer, ScooterLogsSerializer
from django.db.models import Q
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from .models import ScooterAvailability, ScooterLogs
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
# Create your views here.

#Book a scooter
@api_view(['PATCH'])
def book_scooter(request, id):
    scooter = list(ScooterAvailability.objects.filter(id=id).values())
    if scooter[0]['scooter_status'] == 'available':
        ScooterAvailability.objects.filter(id=id).update(scooter_status='booked')
        return Response("Ride Found")
    return Response("Not Found, Please choose another one")
'''
some error s in executing

@api_view(['PATCH'])
def update_table(request, id):
    scooter = list(ScooterAvailability.objects.filter(id=id).values())
    if scooter[0]['scooter_status'] == 'booked':
        ScooterAvailability.objects.filter(id=id).update(scooter_status='available')
        return Response("Thanks for riding with us")
    return Response("Could not find your reservation")


@api_view(['POST','PATCH'])
def payment(request, scooter_id):
    # print(request.method())
    if request.POST:
        ScooterLogs.objects.create(scooter_id=scooter_id, start_time = datetime.now())
    elif request.PATCH:
        update_table(request, scooter_id)
    else:
        return Response("Error")

@api_view(['PATCH'])
def end_reservation(request, id):
    start = ScooterLogs.objects.only('Start_time').filter(id=id).latest('start_time')
    price = (datetime.now()- start).total_seconds()/60
    log = ScooterLogs.objects.filter(id=id).latest('start_time').update(end_time = datetime.now(), rent=price)
    return update_table(request, id)
'''


#View the scooters in nearby area
class AvailableScooters(ListAPIView):
    serializer_class = ScooterAvailabilitySerializer
    model = serializer_class.Meta.model


    def get_queryset(self):
        lng = float(self.request.query_params.get('lng'))
        lat = float(self.request.query_params.get('lat'))
        radius = float(self.request.query_params.get('radius', '20'))/100000

        # for computation purpose considering square instead of a circle
        max_lng, min_lng, max_lat, min_lat = lng+radius, lng-radius, lat+radius, lat-radius

        return self.model.objects.filter(Q(scooter_status = 'available')&
                                         Q(scooter_long__lte = max_lng) &
                                         Q(scooter_long__gte = min_lng) &
                                         Q(scooter_lati__lte = max_lat) &
                                         Q(scooter_lati__gte = min_lat))

