from django.shortcuts import render , get_object_or_404
from django.views import View 
from django.views.generic.edit import CreateView 
from .forms import ContactForm
from django.contrib import messages
from .models import Contact , AboutUs , Service , StatsSection , Portfolio , Category , TeamMember
from blog.models import Post
from django.urls import reverse_lazy

# Create your views here.

class HomeView(View):
    template_name = 'home/index.html'
    form_class = ContactForm  
    

    def get(self,requset , cat_slug = None):
        post = Post.objects.filter(status = 'p')
        about_us = AboutUs.objects.first()
        service = Service.objects.all()
        stats = StatsSection.objects.all()
        portfolio = Portfolio.objects.all()
        categories = Category.objects.all()
        team_member = TeamMember.objects.all()
        form = self.form_class()
        if cat_slug :
            category = get_object_or_404(Category , slug = cat_slug)
            portfolio = Portfolio.objects.filter(category = category)
        

        return render(requset , self.template_name , {

            'form':form , 
            'posts':post ,
            'about_us':about_us,
            'services':service,
            'stats':stats,
            'portfolio':portfolio,
            'category':categories,
            'team_member':team_member,

            })
    
class ContactView(CreateView):
    model = Contact
    form_class = ContactForm   
    template_name = 'home/index.html'
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        messages.success(self.request, "پیام شما با موفقیت ارسال شد 😊")
        return super().form_valid(form)
    

class PortfolioView(View):
    def get(self , request , port_slug):
        return render(request , "home/portfolio-detail.html")

