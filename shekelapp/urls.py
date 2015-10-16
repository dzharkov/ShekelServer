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
    url(r'^items/(?P<item_id>[0-9]+)delete/$', views.delete_item, name='delete_item'),
    # ex: /items/5/edit/
    url(r'^items/(?P<item_id>[0-9]+)/edit/$', views.edit_item, name='edit_item'),
    # ex: /5/items/
    # url(r'^(?P<purchase_id>[0-9]+)/items/$', views.purchase_items, name='purchase_items'),
]