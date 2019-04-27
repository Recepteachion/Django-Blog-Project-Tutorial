from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)
from . import views

urlpatterns = [
	path('',PostListView.as_view(),name="blog-home"),
	path('user/<str:username>',UserPostListView.as_view(),name="user-posts"),
	path('post/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
	path('post/new/',PostCreateView.as_view(),name="post-create"),
	path('post/<int:pk>/update/',PostUpdateView.as_view(),name="post-update"),
	path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post-delete"),
	path("about/",views.about,name="blog-about"),
	path("info/",views.information,name="blog-info"),
	path("address/",views.address,name="blog-address"),
	path("services/",views.services,name="blog-services"),
	path("events/",views.events,name="blog-events"),
	
]