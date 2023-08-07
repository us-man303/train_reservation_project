from django.test import TestCase
from django.urls import reverse
from .models import Train, Reservation

class ReservationTestCase(TestCase):
    def setUp(self):
        self.train = Train.objects.create(name='Express Train', total_seats_first_class=10, total_seats_second_class=20)
    
    def test_reserve_seats_successful(self):
        response = self.client.post(reverse('reserve_seats'), {'family_members': 4, 'preferred_class': 'first class'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reservation.objects.count(), 1)
    
    def test_reserve_seats_invalid_method(self):
        response = self.client.get(reverse('reserve_seats'))
        self.assertEqual(response.status_code, 400)