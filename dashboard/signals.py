# for make automaticly one object 
from home.models import AboutUs
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_aboutus_instance(sender, **kwargs):
    if not AboutUs.objects.exists():
        AboutUs.objects.create()
