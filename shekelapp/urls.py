from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /items/
    url(r'^items/$', views.all_items, name='all_items'),
    # ex: /items/add/
    url(r'^items/add/$', views.add_item, name='add_item'),
    # ex: /items/5/
    url(r'^items/(?P<item_id>[0-9]+)/$', views.view_item, name='view_item'),
    # ex: /items/5/delete/
    url(r'^items/(?P<item_id>[0-9]+)/delete/$', views.delete_item, name='delete_item'),
    # ex: /items/5/edit/
    url(r'^items/(?P<item_id>[0-9]+)/edit/$', views.edit_item, name='edit_item'),

    # ex: /users/
    url(r'^users/$', views.users, name='users'),
    # ex: /users/5/
    url(r'^users/(?P<user_id>[0-9]+)/$', views.view_user, name='view_user'),

    # ex: /receipts/
    url(r'^receipts/$', views.all_receipts, name='all_receipts'),
    # ex: /receipts/5/
    url(r'^receipts/(?P<receipt_id>[0-9]+)/$', views.view_receipt, name='view_receipt'),
    # ex: /receipts/5/items/
    url(r'^receipts/(?P<receipt_id>[0-9]+)/items/$', views.receipt_items, name='receipt_items'),
    # ex: /receipts/add/
    url(r'^receipts/add/$', views.add_receipt, name='add_receipt'),
]
