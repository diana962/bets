from rest_framework import generics
from .models import Bets
from .serializers import BetListSerializer, BetUpdateSerializer, BetCreateSerializer

class BetListApiView(generics.ListAPIView):
    queryset = Bets.objects.all()
    serializer_class = BetListSerializer

class BetCreateApiView(generics.ListCreateAPIView):
    queryset = Bets.objects.all()
    serializer_class = BetCreateSerializer

class BetUpdateApiView(generics.UpdateAPIView):
    queryset = Bets.objects.all()
    serializer_class = BetUpdateSerializer
    lookup_field = 'pk'