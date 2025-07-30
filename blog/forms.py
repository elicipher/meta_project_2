from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content' : forms.Textarea(attrs={'name':'form-message' , 'placeholder':'نظر شما', 'rows':'8'})

        }
        labels ={
            'content':''
        }
class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content' : forms.Textarea(attrs={'name':'form-message' , 'placeholder':'پاسخ شما', 'rows':'8'})

        }
        labels ={
            'content':''
        }