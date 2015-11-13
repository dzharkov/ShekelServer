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

    # ex: event_id/receipts/
    url(r'^event_id/receipts/$', views.event_receipts, name='all_receipts'),
    # ex: event_id/receipts/5/
    url(r'^event_id/(?P<receipt_id>[0-9]+)/$', views.view_receipt, name='view_receipt'),
    # ex: event_id/receipts/add/
    url(r'^event_id/receipts/add/$', views.add_receipt, name='add_receipt'),
    # ex: event_id/5/items/
    url(r'^event_id/(?P<receipt_id>[0-9]+)/items/$', views.receipt_items, name='receipt_items'),
    # ex: event_id/5/3
    url(r'^event_id/([0-9]+)/(?P<item_id>[0-9]+)/$', views.view_item, name='view_item'),
    # ex: event_id/5/items/add
    url(r'^event_id/(?P<receipt_id>[0-9]+)/items/add/$', views.additem, name='additem'),
    # ex: event_id/5/3/edit
    url(r'^event_id/([0-9]+)/(?P<item_id>[0-9]+)/edit/$', views.edititem, name='edititem'),
    # ex: event_id/5/3/delete
    url(r'^event_id/(?P<receipt_id>[0-9]+)/(?P<item_id>[0-9]+)/delete/$', views.deleteitem, name='deleteitem'),
]
