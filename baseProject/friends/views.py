from django.shortcuts import render
from .models import friend_list
from dashboard.models import Login_info_new_p

# Create your views here.
def allFriends(request):
    my_id = request.session.get('user_id')
    friendships = friend_list.objects.filter(user_id=my_id)
    {"id": my_id,
            "name": f"{"Nasim"} {"Wapvcrq"}",
            "email": "nasim@example.com" }
    friends_data = []
    for fr in friendships:
        u = fr.friend_id
        friends_data.append({
            "my_id": fr.user_id.id,
            "id": u.id,
            "name": f"{u.fname} {u.lname}",
            "email": u.email,
        })
    return render(request,"friends/friend_list.html",{"friends":friends_data,"my_id":friendships})