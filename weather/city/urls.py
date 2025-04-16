from django.urls import path
from . import views
urlpatterns=[
    path('w',views.weather,name="weather"),
    path('signup/',views.signup_views,name="signup"),
    path('',views.login_views,name="login"),
    path('logout/',views.logout_views,name="logout"),



    
]