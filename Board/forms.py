from django import forms
from .models import Post, Message
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'category', 'upload']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get('title')
        if text is not None and len(text) < 10:
            raise ValidationError({
                "text": "Тhe text cannot be shorter than 10 characters."
            })
        elif text == title:
            raise ValidationError({"text": "The text cannot duplicate the title"})

        return cleaned_data


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['post', 'author', 'text', 'accepted']


