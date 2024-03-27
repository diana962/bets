from django.urls import path
from .views import BetListApiView, BetCreateApiView, BetUpdateApiView

urlpatterns = [
    path('bets/', BetCreateApiView.as_view()),
    path('bets/history', BetListApiView.as_view()),
    path('events/<int:pk>/', BetUpdateApiView.as_view()),
]
