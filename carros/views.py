from urllib import request
from django.shortcuts import render, redirect
from .models import Carros
from .forms import FormularioCarros


def list_all_cars(request):
    carro = Carros.objects.all()
    data = {}
    data["Carros"] = carro

    return render(request, "blog/home.html", data)


def create_car(request):
    form = FormularioCarros(request.POST or None)
    data = {}
    data["form"] = form

    if form.is_valid():
        form.save()
        return redirect("list_all_cars")

    return render(request, "blog/create.html", data)


def list_one_car(request, pk):
    carro = Carros.objects.get(pk=pk)
    data = {}
    data["carros"] = carro

    return render(request, "blog/postagem.html", data)


def update_car(request, pk):
    data = {}
    carro = Carros.objects.get(pk=pk)
    form = FormularioCarros(request.POST or None, instance=carro)

    if form.is_valid():
        form.save()
        return redirect("/")
    data["form"] = form
    
    return render(request, "blog/update.html", data)


def delete_car(request, pk):
    carro = Carros.objects.get(pk=pk)
    carro.delete()

    return redirect("/")

