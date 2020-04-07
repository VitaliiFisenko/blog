from django import forms

from my_blog.models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ('created_at', )
