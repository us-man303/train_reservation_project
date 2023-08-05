from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=100)
    total_seats_first_class = models.PositiveIntegerField()
    total_seats_second_class = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'reservation'

class Reservation(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    cabin_class = models.CharField(max_length=20)  # "first class" or "second class"
    seat_numbers = models.CharField(max_length=100)
    reservation_id = models.CharField(max_length=10, unique=True)
    total_fare = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Reservation ID: {self.reservation_id}, Train: {self.train}"
    
    class Meta:
        app_label = 'reservation'
