# from django.shortcuts import render
# from django.db import models
# Create your views here.

# import json
from annoying.decorators import ajax_request
from django.http import HttpResponse
from .models import Item, MyUser


# def index(request):
#     latest_items_list = Item.objects.all()[:5]
#     output = '{ "Item": [ {' + "}, {".join(
#         [str('"name": "' + p.name + '" , "cost": ' + str(p.cost)) for p in latest_items_list]) + '} ] }'
#     return HttpResponse(output)


@ajax_request
def index(request):
    output = Item.objects.all()[:5]
    return HttpResponse(output)
    # TODO выдавать output через ajax


def all_items(request):
    return HttpResponse("You're looking at items.")


def add_item(request):
    # i = Item()
    # i.name = request.GET['name']
    # i.cost = request.GET['cost']
    # i.customer = request.GET['customer']
    # i.consumers = request.GET['consumers_ids']
    # i.save()
    print(requ)
    return HttpResponse("OK")
    # TODO принимать параметры в add, из POST, проверять чтобы не было лишних символов escape string


def view_item(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)


def edit_item(request):
    return HttpResponse("You're looking at items.")


def delete_item(request):
    return HttpResponse("You're looking at items.")


def purchase_items(request, purchase_id):
    return HttpResponse("You're looking at items of purchase %s." % purchase_id)


