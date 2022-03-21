from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('businesses/', views.businesses, name='businesses'),
    path('hood/', views.hood, name='hood'),
    path('profile/', views.profile, name='profile'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/register/', views.register_user, name='register'),
    path('accounts/logout/', views.logout_user, name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)