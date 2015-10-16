# from django.shortcuts import render
# Create your views here.

# import json
from annoying.decorators import ajax_request
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, Http404
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from django.core import serializers

from .models import Item, MyUser

@ajax_request
def json_handler(request, data):
    if isinstance(data, models.Model):
        return data.as_dict()
    elif isinstance(data, dict):
        return data
    else:
        return {'result': 1, 'data': list(map(lambda x: x.as_dict(), data))}


def index(request):
    latest_items_list = Item.objects.all()[:5]
    output = '{ "Item": [ {' + "}, {".join(
        [str('"name": "' + p.name + '" , "cost": ' + str(p.cost)) for p in latest_items_list]) + '} ] }'
    return HttpResponse(output)


@csrf_exempt
def all_items(request):
    try:
        data = Item.objects.all()
        return json_handler(request, data)
    except Exception as e:
        print(e)

    # TODO выдавать output через ajax


def add_item(request):
    # i = Item()
    # i.name = request.GET['name']
    # i.cost = request.GET['cost']
    # i.customer = request.GET['customer']
    # i.consumers = request.GET['consumers_ids']
    # i.save()
    print(request.GET['name'])
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


# def request_handler(request, model_name, **kwargs):
#     method = request.META["REQUEST_METHOD"]
#     models = {
#         "item": Item,
#         "user": MyUser
#     }
#
#     if model_name not in models:
#         raise Http404()
#     model = models[model_name]
#     data = process_request(request, method=method, model=model, **kwargs)
#     return json_handler(request, data)