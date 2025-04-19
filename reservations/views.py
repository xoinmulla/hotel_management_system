from django.shortcuts import render
from .models import Hotel, Room


def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'home.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel, is_available=True)
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'rooms': rooms})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import Reservations, Room
from django.contrib.auth.models import User

def manage_reservations(request):
    if request.method == 'POST':
        # Handle form submission
        user_id = request.POST.get('user')
        room_id = request.POST.get('room')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        # Create reservation logic here...

    reservations = Reservations.objects.all()
    users = User.objects.all()
    rooms = Room.objects.all()
    return render(request, 'manage_reservations.html', {
        'reservations': reservations,
        'users': users,
        'rooms': rooms
    })
