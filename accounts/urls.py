from django.urls import path
from . import views

urlpatterns = [
    path("c/login", views.login, name="clogin"),
    path("c/register", views.register, name="cregister"),
    path('logout', views.logout_view, name='logout'),
    path('profile/create', views.create_profile, name='create_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile')
]