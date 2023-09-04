from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from movies.models import Shows

def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    

def home(request): 
    return render(request, 'home.html')

def signin(request):
    # if request.user.is_authenticated:
    #     return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/locations')
            # locations = Shows.objects.all().order_by().values('theatre_location').distinct()
            # return render(request,"locations.html",{'locations':locations})
            # return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    



def profile(request): 
    return render(request, 'profile.html')

def signout(request):
    logout(request)
    return redirect('/')

def shows(request):
    shows = Shows.objects.all()
    return render(request,"show.html",{'shows':shows})

def locations(request):
    locations = Shows.objects.all().order_by().values('theatre_location').distinct()
    return render(request,"locations.html",{'locations':locations})

def theater_detail(request,theater_location):
    movies = Shows.objects.all().filter(theatre_location=theater_location)
    return render(request,"movies.html",{'movies':movies})

def seats(request,movie_name): 
    movies = Shows.objects.all().get(movie_name=movie_name)
    return render(request, "seats.html",{'movies':movies})
