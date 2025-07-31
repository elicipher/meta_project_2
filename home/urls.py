from django.urls import path
from .views import HomeView , ContactView , PortfolioView

app_name = 'home'

urlpatterns = [
    path('home/', HomeView.as_view() , name='home'),
    path('', HomeView.as_view() , name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('portfolio/', PortfolioView.as_view(), name='contact'),
]