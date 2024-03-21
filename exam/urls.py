"""
URL configuration for exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from medics import views
from django.urls import path,include

urlpatterns = [
        path('',views.signup,name='signup'),
        path('login/',views.login_page,name='login'),
        path('logout/', views.logout_view,name='logout'),
        path('search/', views.search_item, name='search_item'),
        path('home',views.home,name='home'),
        path('create/',views.product_create,name='createmed'),
        path('retrieve/',views.product_read,name='listmed'),
        path('update/<int:pk>/',views.product_update,name='updatemed'),
        path('delete/<int:pk>',views.product_delete,name='deletemed'),
        path('medicsapi/', include('medicsapi.urls')),
    ]