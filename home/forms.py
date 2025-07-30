from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control con-validate','id':'contact-name','placeholder':'نام' , 'minlength': '3'}),
            'email': forms.EmailInput(attrs={'type':'email','class':'form-control con-validate','id':'contact-name','placeholder':'ایمیل' , 'minlength': '3'}),
            'message': forms.Textarea(attrs={'type':'text','class':'form-control con-validate','id':'contact-name','placeholder':'چطور میتونم کمکتون' , 'minlength': '3'}),
        }