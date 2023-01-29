from django_filters import FilterSet
from .models import Post, Message


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {'title': ['icontains'],
                  'category': ['exact']
                  }


class MessageFilter(FilterSet):

    class Meta:
        model = Message
        fields = {'post': ['exact'],
                  'author': ['exact'],
                  'accepted': ['exact'],
                  }