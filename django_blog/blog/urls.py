from django.urls import path
from .views import AboutView, PostListView, PostDetailView,

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
