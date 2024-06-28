"""
URL configuration for multilang_site project.

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
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from main import views

# les différentes urls de l'application avec le pattern pour afficher la langue sur le navigateur
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.article_list, name='article-list'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('articles/<int:id>/', views.article_detail, name='article-detail'),
    path('articles/add/', views.article_create, name='article-create'),
    path('articles/<int:id>/change/', views.article_update, name='article-update'),
    path('articles/<int:id>/delete/', views.article_delete, name='article-delete'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
)
