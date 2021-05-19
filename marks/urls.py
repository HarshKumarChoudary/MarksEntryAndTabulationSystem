from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from marks import views
#from app.forms import loginform,passwordchangeform,passwordresetform,setpasswordform

urlpatterns = [
    path('', views.home.as_view(),name='home'),
    path('leaderboard/',views.leaderboard.as_view(),name='leaderboard'),
    path('asc/',views.asc,name='ASC'),
]  