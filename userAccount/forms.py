from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    images = forms.ImageField()
    images.widget.attrs.update({'multiple':True,'accept':'image/*'})
    class Meta:
        model = Post
        fields = ['description','price','images']