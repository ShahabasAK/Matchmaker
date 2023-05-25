from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Max
from django.contrib.auth import logout

def signn1(request):
    if request.method == "POST":
        # Process the signup form and create the user
        b = request.POST.get('email')
        c = request.POST.get('password')
        ab = signn(email=b, password=c)
        ab.save()

        # Set the user's ID in the session
        request.session['id'] = ab.id

        msg = {'msg': 'User Registered'}
        return render(request, "index.html", msg)
    else:
        return render(request, "signn.html")

 
def login(request):
    if request.method == "POST":
        b = request.POST.get('email')
        c = request.POST.get('password')
        msg = {'msg': 'User Not Found'}
        obj1=signn.objects.filter(email=b,password=c)
        
        if obj1.filter(email=b,password=c):
            for i in obj1:
                id=i.id
                request.session['id']=id
            return render(request, "index.html")
        else:
            return render(request, "signn.html",msg)
    else:
        return render(request, "signn.html")
    

        


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def team(request):
    return render(request,"team.html")

def contact(request):
    return render(request,"contact.html")

def explore(request):
    return render(request,"explore.html")

def mates(request):
    id=request.session['id']
    requests = Request_users.objects.filter(idreciever=id,status='Yes')
    
    return render(request, 'mates.html', {'requests': requests})


 

def profile(request):
    id=request.session['id']
    a=signn.objects.filter(id=id)
     
    return render(request,"profile.html",{'a':a})

def edit(request):
    id=request.session['id']
    a=signn.objects.get(id=id)
    if request.method == "POST":
        ab = request.POST.get('username')
        b = request.POST.get('email')
        c = request.POST.get('password')
        d = request.FILES.get('photo')
        e = request.POST.get('name')
        f = request.POST.get('bio')
        g = request.POST.get('date')
        h = request.POST.get('gender')
        j = request.POST.get('qualification')
        k = request.POST.get('number')
        a.username=ab
        a.email=b
        a.password=c
        a.photo=d
        a.name=e
        a.bio=f
        a.dob=g
        a.gender=h
        a.qualification=j
        a.number=k
        a.save()
        msg = {'msg': 'User Updated'}
        return render(request, "index.html", msg)
    else:
        return render(request, "edit.html")


def logout_view(request):
    logout(request)
    return redirect('/')


def request(request):
    return render(request,"request.html")

def explore(request):
    user = request.session['id']
    a = signn.objects.exclude(id=user)
    return render(request, "explore.html", {"a": a})


def send_request(request,receiver_id):
    sender_id=request.session['id']
    sender = signn.objects.get(id=sender_id)
    receiver = signn.objects.get(id=receiver_id)
    if Request_users.objects.filter(idrequest=sender, idreciever=receiver):
        msg='Already Requested'
        user = request.session['id']
        a = signn.objects.exclude(id=user)
        all={'a':a,'msg':msg}
        return render(request, "explore.html",all)

    # Create a new request

    request_obj = Request_users.objects.create(idrequest=sender, idreciever=receiver)
    
    # Redirect to the request.html page or any other desired page
    return redirect('/explore')
def request_page(request):
    id=request.session['id']
    requests = Request_users.objects.filter(idreciever=id,status='No')
    return render(request, 'request.html', {'requests': requests})

def acceptrequest(request,id):
    a=Request_users.objects.get(id=id)
    a.status='Yes'
    a.save()
    return redirect('/viewrequests')

def rejectrequest(request,id):
    a=Request_users.objects.get(id=id)
    a.status='rejected'
    a.save()
    return redirect('/viewrequests')  