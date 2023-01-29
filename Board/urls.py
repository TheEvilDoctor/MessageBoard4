from django.urls import path

from .views import PostDetail, PostList, CreatePost, UpdatePost, DeletePost, Search, CreateMessage


urlpatterns = [
   path('', PostList.as_view(), name='posts'),
   path('<int:pk>/', PostDetail.as_view(), name='post'),
   path('create/', CreatePost.as_view(), name='create'),
   path('create_message/', CreateMessage.as_view(), name='message'),
   path('search/', Search.as_view(), name='search'),
   path('<int:pk>/edit/', UpdatePost.as_view(), name='edit'),
   path('<int:pk>/delete/', DeletePost.as_view(), name='delete')
]
