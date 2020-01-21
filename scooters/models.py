from django.db import models

# Create your models here.

# class ScooterDetails(models.Model):
#     scooter_numplate = models.CharField(max_length=10)
#     scooter_color = models.CharField(max_length=10)
#     scooter_company = models.CharField(max_length=20)
#
#     def __str__(self):
#         return str(self.id)


class ScooterAvailability(models.Model):
    Status = (
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('inservice', 'In-service'),
    )
    scooter_lati = models.FloatField()
    scooter_long = models.FloatField()
    scooter_status = models.CharField(max_length=10, choices=Status, default='available')

    def __str__(self):
        return str(self.id)


class ScooterLogs(models.Model):
    scooter_id = models.ForeignKey(ScooterAvailability, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    rent = models.FloatField(null=True)