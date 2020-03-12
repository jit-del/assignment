from django.contrib import messages
from django.shortcuts import render, redirect
import requests
import json
# Create your views here.

username = "admin"
password = "admin"


def index(request):
    return render(request, "index.html")


def display(request):
    res = requests.get("http://127.0.0.1:8000/create/")
    data = res.json()
    return render(request, "display.html", {"data":data})


def create(request):
    global username
    if request.method == 'POST':
        username = username
        note = request.POST["note"]
        data = {"username": username, "note": note}
        json_data = json.dumps(data)
        res = requests.post("http://127.0.0.1:8000/create/", data=json_data)
        messages.success(request, "note added successfully.")
        return redirect('display')
    else:
        return render(request, "create.html")


def updateshow(request, pk):
    res = requests.get("http://127.0.0.1:8000/updateshow"+str(pk)+"/")
    print(res.status_code)
    data = res.json()
    return render(request, 'display.html', {"udata":data})


def update(request, pk):
    if request.method == 'POST':
        note = request.POST["note"]
        data = {"note": note}
        json_data = json.dumps(data)
        res = requests.put("http://127.0.0.1:8000/update"+str(pk)+"/", data=json_data)
        messages.success(request, "note updated successfully.")
        return redirect('display')
    else:
        return redirect('display')


def login(request):
    global username, password
    if request.method == 'POST':
        u = request.POST["username"]
        p = request.POST["password"]
        if u == username and p == password:
            return redirect('index')
        else:
            return render(request, 'login.html', {"msg":"invalid password !"})
    else:
        return render(request, 'login.html')


def filter(request):
    id = request.POST["id"]
    d = request.POST["date"]
    if d:
        res = requests.get("http://127.0.0.1:8000/filterdate"+str(d)+"/")
        data = res.json()
        return render(request, "display.html", {"data": data})
    else:
        res = requests.get("http://127.0.0.1:8000/filter"+id+"/")
        data = res.json()
        return render(request, "display.html", {"data": data})
