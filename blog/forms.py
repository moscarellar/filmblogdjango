from .models import Comment, Post, User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)