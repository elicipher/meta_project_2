from django.forms.models import inlineformset_factory
from home.models import AboutUs , Social , Contact
from django import forms
from home.models import Portfolio , TeamMember
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from django.db import models
from blog.models import Post , Comment
from django_prose_editor.fields import ProseEditorField


SocialLinkFormSet = inlineformset_factory(
    AboutUs,
    Social,
    fields=['icon','link'],
    extra= 4,
    can_delete= False,
)

SocialTeamMemberFormset = inlineformset_factory(
    TeamMember,
    Social,
    fields=['icon','link'],
    extra= 4,
    can_delete= False,

)

class PortfolioForm(forms.ModelForm):
    history = JalaliDateField(widget=AdminJalaliDateWidget(attrs={'class': 'form-control'}))
    class Meta:
        model = Portfolio
        fields = '__all__'

   


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('reply',)

    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)
        readonly_fields = ['name','email','message','replyed','send_time','reply_time']

        for field in readonly_fields:

            if field == 'message':
                widget = forms.Textarea
            elif isinstance(self.instance._meta.get_field(field), models.BooleanField):
                widget = forms.CheckboxInput()
            else:
                widget = forms.TextInput

            self.fields[field] = forms.CharField(
                initial=getattr(self.instance, field),
                disabled=True,
                required=False,
                widget=widget
 
            )


class PostForm(forms.ModelForm):
    description = ProseEditorField()
    class Meta:
        model = Post
        fields = '__all__'




class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'متن پاسخ',
        }

class CommentConfirmeForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['confirme']
        labels = {
            'confirme': 'تایید',
        }
