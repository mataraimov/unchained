from django.urls import path
from .views import PostListViev, PostCreateView,PostDetailView , PostUpdateView,PostDeleteView


urlpatterns = [
    path('',PostListViev.as_view(), name ='post-list'),
    path('create/',PostCreateView.as_view(), name='create'),
    path('post/<int:pk>',PostDetailView.as_view(), name='post-detail' ),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update' ),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete' ),
]