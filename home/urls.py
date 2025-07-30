from django.urls import path
from .views import HomeView , ContactView

app_name = 'home'

urlpatterns = [
    path('home/', HomeView.as_view() , name='home'),
    path('', HomeView.as_view() , name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]