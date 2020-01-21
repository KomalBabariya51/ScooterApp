from django.urls import path
from . import views


urlpatterns = [
    path('available/', views.AvailableScooters.as_view(), name='scootersAt'),
    path('book/<int:id>', views.book_scooter, name='book'),
    path('endreservation/<int:id>', views.end_reservation, name='end'),
    path('payment/<int:scooter_id>', views.payment, name='pay')

]