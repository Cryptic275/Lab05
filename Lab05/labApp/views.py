from django.shortcuts import render
from django.http import HttpResponse
from django import forms


# Create your views here.
class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class PersonForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

people = []

def display(request):
    return render(request, "labApp/display.html", {
        "people": people
    })


def add(request):
    if request.method == "POST":
        form = PersonForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            person = Person(username, password)
            people.append(person)
        
        else:   
            return render(request, "labApp/add.html", {
                "form": form
            })
    return render(request, "labApp/add.html", {
        "form": PersonForm()
    })
