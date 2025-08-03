from django.urls import path
from .views import HomeView , ContactView, PortfolioView

app_name = 'home'

urlpatterns = [
    
    path('contact/', ContactView.as_view(), name='contact'),
    path('<slug:cat_slug>/', HomeView.as_view() , name='home'),
    path('portfolio/<slug:port_slug>/', PortfolioView.as_view(), name='portfolio-detail'),
    path('', HomeView.as_view() , name='home'),

]