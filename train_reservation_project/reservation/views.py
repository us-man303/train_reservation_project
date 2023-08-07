import random
import string
from django.shortcuts import render
from django.http import JsonResponse
from .models import Train, Reservation

# Create your views here.
def reserve_seats(request):
    if request.method == 'POST':
        try:
            family_members = int(request.POST.get('family_members'))
            preferred_class = request.POST.get('preferred_class')

            # Retrieve the selected train
            train = Train.objects.get(name='Express Train')  # You should modify this to get the desired train
            
            # Determine the total number of seats needed
            if preferred_class == 'first class':
                total_seats_needed = family_members
            else:
                total_seats_needed = 2 * family_members  # Assuming each cabin in second class has 2 seats
            
            # Check seat availability
            if preferred_class == 'first class':
                if train.total_seats_first_class >= total_seats_needed:
                    # Enough seats available, proceed with reservation
                    # Calculate total fare based on cabin class and number of family members
                    total_fare = 100 * total_seats_needed  # Placeholder fare calculation
                    
                    # Perform seat reservation logic here
                    # For simplicity, let's assume seats are reserved in sequential order
                    reserved_seats = []
                    for _ in range(total_seats_needed):
                        reserved_seats.append(f"1A")
                    
                    # Generate reservation ID
                    reservation_id = generate_random_id(5)

                    # Create reservation record
                    reservation = Reservation.objects.create(
                        train=train,
                        cabin_class=preferred_class,
                        seat_numbers=', '.join(reserved_seats),
                        reservation_id=reservation_id,
                        total_fare=total_fare
                    )

                    return JsonResponse({'reservation_id': reservation_id, 'message': 'Reservation successful'})
                else:
                    return JsonResponse({'error': 'Not enough seats available in the chosen cabin class'})
            else:
                if train.total_seats_second_class >= total_seats_needed:
                    # Enough seats available, proceed with reservation
                    # Calculate total fare based on cabin class and number of family members
                    total_fare = 80 * total_seats_needed  # Placeholder fare calculation
                    
                    # Perform seat reservation logic here
                    # For simplicity, let's assume seats are reserved in sequential order
                    reserved_seats = []
                    for _ in range(total_seats_needed):
                        reserved_seats.append(f"2A")
                    
                    # Generate reservation ID
                    reservation_id = generate_random_id(5)

                    # Create reservation record
                    reservation = Reservation.objects.create(
                        train=train,
                        cabin_class=preferred_class,
                        seat_numbers=', '.join(reserved_seats),
                        reservation_id=reservation_id,
                        total_fare=total_fare
                    )

                    return JsonResponse({'reservation_id': reservation_id, 'message': 'Reservation successful'})
                else:
                    return JsonResponse({'error': 'Not enough seats available in the chosen cabin class'})
            
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request method'})



def generate_random_id(length):
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id
