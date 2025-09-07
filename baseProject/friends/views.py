from django.shortcuts import render
from .models import friend_list
from dashboard.models import Login_info_new_p

# Create your views here.
def allFriends(request):
    my_id = request.session.get('user_id')
    
    all_users = Login_info_new_p.objects.all()
    user_data = {}
    for u in all_users:
        user_data[u.id] = {0:u.email,1:u.fname,2:u.lname}
        
    
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
    return render(request,"friends/friend_list.html",{"friends":friends_data,"my_id":friendships,"user_data":user_data})

def friend_req(request,u_id):
    my_id = request.session.get('user_id')
    user = Login_info_new_p.objects.get(id=my_id)
    friend = Login_info_new_p.objects.get(id=u_id)
    f_list = friend_list(user_id=user,friend_id=friend)
    f_list.save()
    return render(request,"friends/friend_list.html",{"my_id":my_id})