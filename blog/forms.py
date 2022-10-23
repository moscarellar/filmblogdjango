from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'featured_image',
                  'content', 'author')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':
                                            'Give it a catchy title'}),
            'excerpt': forms.TextInput(attrs={'placeholder':
                                              'E.g. My first ever post'}),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '',
                       'id': 'user', 'type': 'hidden'}),
        }