from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    fullname = forms.CharField(max_length = 30, required = True)
    email = forms.EmailField(max_length = 30, help_text = 'Required. Enter the Valid Email')

    class Meta:
        model = User
        fields = ['username','fullname','email','password1','password2']


    #     class MovieForm(forms.Form):
    # movie_name = forms.CharField(label = 'Enter movie name', max_length = 100)
    # year = forms.CharField(label = 'Year')


class Country(forms.Form):
        news = forms.CharField(label = "choose the choice")
        country = forms.CharField(label = "country")
        category = forms.CharField(label = "category", required = False)


class Source(forms.Form):
    news = forms.CharField(label = "Its either top news or headlines")
    source = forms.CharField(label = "source")
    

class KeyWord(forms.Form):
    news = forms.CharField(label = "news content")
    q = forms.CharField(label = "enter keyword")
    fromdate = forms.CharField(label='from date')
    todate = forms.CharField(label = "enter to date", required = False)
