from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import Country, Source, KeyWord
import requests

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url = 'login')
def mainpage(request):
    return render(request, 'mainpage.html')


@login_required(login_url = 'login')
def country(request):
    if request.method == "POST":
        form = Country(request.POST)
        if form.is_valid():
            newscontent = form.cleaned_data['news']
            country = form.cleaned_data['country']
            category = form.cleaned_data['category']
            apikey = '65e463596f694c6b9f08f0821bd7917f'
            print(newscontent)
            print(country)
            response = requests.get('https://newsapi.org/v2/'+ newscontent + '?' + 'country=' + country + '&category=' + category +'&apiKey=' + apikey)
            print(response.json())
            data = response.json()
            return render(request, template_name = 'display.html', context = {
                # 'totalResults': data['totalResults'],
                'articles' : data['articles'],
            })
    else:
        form = Country()
        return render(request, 'central.html', {'form': form})

@login_required(login_url = 'login')
def source(request):
    if request.method == 'POST':
        form = Source(request.POST)
        if form.is_valid():
            newscontent = form.cleaned_data['news']
            source = form.cleaned_data['source']
            apikey = '65e463596f694c6b9f08f0821bd7917f'
            print(newscontent + " "+ source)
            response = requests.get('https://newsapi.org/v2/' + newscontent + '?' + 'sources=' + source + '&apikey=' + apikey)
            print(response.json())
            data = response.json()
            return render(request, template_name = 'display.html', context = {
                # 'totalResults': data['totalResults'],
                'articles' : data['articles'],
            })
    else:
        form = Source()
        return render(request, 'central.html', {'form': form})

@login_required(login_url = 'login')
def date(request):
    if request.method == 'POST':
        form = KeyWord(request.POST)
        print("Hii")
        if form.is_valid():
            newscontent = form.cleaned_data['news']
            q = form.cleaned_data['q']
            fromdate = form.cleaned_data['fromdate']
            todate = form.cleaned_data['todate']
            print(newscontent + " " + q + " " + fromdate + " "+ todate)
            apikey = '65e463596f694c6b9f08f0821bd7917f'
            # print(newscontent + " "+ source)
            response = requests.get('https://newsapi.org/v2/' + newscontent + '?' + 'q=' + q + '&from=' + fromdate + '&to=' +todate +' &apikey=' + apikey)
            print(response.json())
            data = response.json()
            return render(request, template_name = 'display.html', context = {
                # 'totalResults': data['totalResults'],
                'articles' : data['articles'],
            })
    else:
        form = KeyWord()
        return render(request, 'central.html', {'form': form})
  