from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('friends/',views.allFriends,name="friends"),
    path('friend_req/<int:u_id>',views.friend_req,name="send_friend_request"),  
      
]
