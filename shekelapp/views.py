# from django.shortcuts import render
# from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, Http404
# from django.core import serializers

# import json
from annoying.decorators import ajax_request
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
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
        return HttpResponse("Exception")


def add_item(request):
    try:
        i = Item()
        i.name = request.GET['name']
        i.cost = request.GET['cost']
        i.customer = MyUser.objects.get(id=int(request.GET['customer']))
        i.save()
    except Exception as e:
        print(e)
    return HttpResponse("Item was added")


@csrf_exempt
def view_item(request, item_id):
    try:
        data = Item.objects.get(id=item_id)
        return json_handler(request, data)
    except Exception as e:
        print(e)
        return HttpResponse("Exception")


def edit_item(request, item_id):
    try:
        i = Item.objects.get(id=item_id)
        i.name = request.GET['name']
        i.cost = request.GET['cost']
        i.customer = MyUser.objects.get(id=int(request.GET['customer']))
        i.save()
    except Exception as e:
        print(e)
    return HttpResponse("Item %s was edited" % item_id)


def delete_item(request, item_id):
    Item.objects.get(id=item_id).delete()
    return HttpResponse("Item %s was deleted." % item_id)


def users(request):
    try:
        data = MyUser.objects.all()
        return json_handler(request, data)
    except Exception as e:
        print(e)
        return HttpResponse("Exception")


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
