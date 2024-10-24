from django.shortcuts import render
from .models import Travels

def index(request):
    return render(request, 'travel/index.html')

def about(request):
    return render(request, 'travel/about.html')

def deals(request):
    return render(request, 'travel/deals.html')

def reservation(request):
    return render(request, 'travel/reservation.html')

def travels(request):
    return render(request, 'travel/travels.html')

def travel_list(request):
    travels = Travels.objects.all()  # Fetch all travel entries
    return render(request, 'travel/travels.html', {'travels': travels})