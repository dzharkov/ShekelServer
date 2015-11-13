# from django.shortcuts import render
# from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, Http404
# from django.core import serializers

# import json
from annoying.decorators import ajax_request
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from .models import Item, MyUser, Receipt


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
    return json_handler(request, latest_items_list)
    # output = '{ "Item": [ {' + "}, {".join(
    #    [str('"name": "' + p.name + '" , "cost": ' + str(p.cost)) for p in latest_items_list]) + '} ] }'
    # return HttpResponse(output)


@csrf_exempt
def all_items(request):
    data = Item.objects.all()
    return json_handler(request, data)


def add_item(request):
    i = Item()
    i.name = request.GET['name']
    i.cost = request.GET['cost']
    i.customer = MyUser.objects.get(id=int(request.GET['customer']))
    consumer_ids_list = list(map(int, request.GET['consumer_ids'].split(",")))
    consumers = list(MyUser.objects.filter(id__in=consumer_ids_list).all())
    i.save()
    i.consumers.clear()
    i.consumers.add(*consumers)
    i.save()
    return {'result': 1}


@csrf_exempt
def view_item(request, item_id):
    # try:
    data = Item.objects.get(id=item_id)
    return json_handler(request, data)
    # except Exception as e:
    #    print(e)
    # return HttpResponse("Exception")


def edit_item(request, item_id):
    i = Item.objects.get(id=item_id)
    i.name = request.GET['name']
    i.cost = request.GET['cost']
    i.customer = MyUser.objects.get(id=int(request.GET['customer']))
    consumer_ids_list = list(map(int, request.GET['consumer_ids'].split(",")))
    consumers = list(MyUser.objects.filter(id__in=consumer_ids_list).all())
    i.save()
    i.consumers.clear()
    i.consumers.add(*consumers)
    i.save()
    return {'result': 1}
    # return HttpResponse("%s" % str(int(i.cost)/17))


def delete_item(request, item_id):
    Item.objects.get(id=item_id).delete()
    return {'result': 1}


def users(request):
    data = MyUser.objects.all()
    return json_handler(request, data)


@csrf_exempt
def view_user(request, user_id):
    data = MyUser.objects.get(id=user_id)
    return json_handler(request, data)


def all_receipts(request):
    data = Receipt.objects.all()
    return json_handler(request, data)


def view_receipt(request, receipt_id):
    data = Receipt.objects.get(id=receipt_id)
    return json_handler(request, data)


def receipt_items(request, receipt_id):
    data = Receipt.objects.get(id=receipt_id).items.all()
    return json_handler(request, data)


def add_receipt(request):
    i = Receipt()
    i.name = request.GET['name']
    i.owner = MyUser.objects.get(id=int(request.GET['owner']))
    consumer_ids_list = list(map(int, request.GET['consumer_ids'].split(",")))
    consumers = list(MyUser.objects.filter(id__in=consumer_ids_list).all())
    items_ids_list = list(map(int, request.GET['items_ids'].split(",")))
    items = list(Item.objects.filter(id__in=items_ids_list).all())
    count = 0
    for i in items:
        count += i.cost
    i.cost = count
    i.save()
    i.shared.clear()
    i.shared.add(*consumers)
    i.items.clear()
    i.items.add(*items)
    i.save()
    return {'result': 1}






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
