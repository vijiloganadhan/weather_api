from django.shortcuts import render , redirect
import requests
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login ,logout

# Create your views here.
def weather(request):
    e=''
    name=request.GET.get('name')
    api_keys="1844f66645a1045ef731cfd3574c2d99"
    URL=f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_keys}"
    res=requests.get(url=URL)
    data=res.json()
    print(data)
    temp1=data['main']['temp']-273.15
    temp=int(temp1)
    if  10<=temp <30:
        e='🌞'
    elif 0<=temp <10:
        e='⛅'
    elif temp <0:
        e='❄️'
    else:
        e=' Heavy heat'
    mintemp=data['main']['temp_min']-273.15
    maxtemp=data['main']['temp_max']-273.15

    

    context={
        'e':e,
        'name':name,
        'data':data,
        'temp':temp,
        'min':mintemp,
        'max':maxtemp
    }
    
    return render(request,'weather.html',context)
def signup_views(request):
    if request.user.is_authenticated:
        return redirect('login')
    if request.method=="POST":
        name=request.POST.get('un')
        email=request.POST.get('e')
        pw1=request.POST.get('p1')
        pw2=request.POST.get('p2')
        if pw1==pw2:
            if not User.objects.filter(username=name):
                User.objects.create_user(username=name,email=email,password=pw1)
                return redirect('login')
            else:
                return render(request,'signup.html',{'msg':'user name already present'})
        else:
            return render(request,'signup.html',{'msg':'Invalid password '})

           
    return render(request,'signup.html')


def login_views(request):
    if request.method=='POST':
        name=request.POST.get('un')
        pw1=request.POST.get('p1')
        user=authenticate(request,username=name ,password=pw1)
        if user is not None:
            login(request,user)
            return redirect('weather')
        return render(request,'login.html',{'msg':'invalid creditials '})
    return render(request,'login.html')

def logout_views(request):
    logout(request)
    return redirect('signup')