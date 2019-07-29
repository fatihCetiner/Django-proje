from django import forms
from .models import Post


class PostForm(forms.ModelForm):# forms.ModelForm dan kalıtım sağladık
    
    class Meta:
        model = Post
        fields = [
                'title',
                'content',
                'image',
                
                ]
        
    