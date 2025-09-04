from django.shortcuts import render
from django.http import JsonResponse
from .models import GFG

def home(request):
    return render(request , 'hotel/home.html')


def get_hotels(request):
    try:
        ans_objects = GFG.objects.all()
        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc':
                ans_objects = ans_objects.order_by("hotel_price")
            elif sort_by_value == 'dsc':
                ans_objects  = ans_objects.order_by("-hotel_price")
            if request.GET.get("amount"):
                amount = request.GET.get("amount")
                ans_objects = ans_objects.filter(hotel_price__lte=amount)
        payload = []
        for ans in ans_objects:
            payload.append({
                'name' : ans.hotel_name , 
                'price' : ans.hotel_price , 
                'description' : ans.hotel_description 
            })
        return JsonResponse(payload , safe=False)

    except Exception as e:
        print(f"we are here {e}")
        
    return JsonResponse({'message' : 'something went wrong' })    

