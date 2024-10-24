from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView
from .views import add_good
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/password/', PasswordChangeView.as_view(), name='password_change'),
    path('add/', views.add_good, name='add_good'),
    path('edit/<int:good_id>/', views.edit_good, name='edit_good'),
    path('delete/<int:good_id>/', views.delete_good, name='delete_good'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)