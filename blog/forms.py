from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget



class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#
# class UpdatePost(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorWidget)
#     class Meta:
#         model = Post
#         fields = ['title', 'description', 'image']


class CreateUpdatePost(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'description', 'image']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields= ['body']

