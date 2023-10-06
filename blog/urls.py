from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:login'), name='logout'),
    path('posts/', views.HomeView.as_view(template_name='home/index.html'), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(template_name='home/post.html'), name='post_detail'),
    path('register/', views.SignUpView.as_view(template_name='home/register.html'), name='register'),
    path('posts/new/',views.CreatePostView.as_view(template_name='home/post_form.html'), name='create_post'),
    path('post/<int:pk>/update', views.EditPostView.as_view(template_name='home/post_form.html'), name='edit_post'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(template_name='home/post_confirm_delete.html'), name='delete_post'),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name='about'),
    path("contact-us/", views.ContactView.as_view(), name='contact'),


]


