from django import forms
from django.shortcuts import render

tasks = ["eat", "drink", "sleep"]

class NewTaskFrom(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskFrom()
    })