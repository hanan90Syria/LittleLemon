from django.shortcuts import render
from django.http import HttpResponse
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import generics,views,permissions,status,viewsets
from .models import Booking,Menu
# Create your views here.
def sayHello(request):
    return HttpResponse("Hello World")

	
def index(request):
    return render(request,'index.html',{})
	
	

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
	
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView ):	 
       queryset = Menu.objects.all()
       serializer_class = MenuSerializer
       permission_classes = [permissions.IsAuthenticated] 
	
class BookingViewSet(viewsets.ModelViewSet):
       queryset = Booking.objects.all()
       serializer_class = BookingSerializer
       permission_classes = [permissions.IsAuthenticated] 