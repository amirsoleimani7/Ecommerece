from django.shortcuts import render
from django.http import JsonResponse


def get_hotel(request):




    return render(request , 'hotel/get_hotels.html' , context={})

