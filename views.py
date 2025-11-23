from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# 1. Static HTML View
def index(request):
    return render(request, 'index.html', {})

# 2. Menu API (Generics)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # Allow anyone to read, but only authenticated users to create
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# 3. Booking API (ViewSet)
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] # Must be logged in to book
