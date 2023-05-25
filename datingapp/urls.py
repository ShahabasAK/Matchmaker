from django.urls import path 
from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    path('', views.signn1, name="signn"),
    path('login',views.login, name="login"),
    path('index',views.index,name="index"),
    path('about',views.about,name="about"),
    path('team',views.team,name="team"),
    path('contact',views.contact,name="contact"),
    path('explore',views.explore,name="explore"),
    path('mates',views.mates,name="mates"),
    path('profile',views.profile,name="profile"),
    path('edit',views.edit,name="edit"), 
    path("request",views.request,name="request"),
    path("logout",views.logout_view,name="logout"),
    path('request/<int:receiver_id>/',views.send_request),
    path('viewrequests',views.request_page),
    path('accept/<int:id>/',views.acceptrequest),
    path('reject/<int:id>/',views.acceptrequest),
    
    
]