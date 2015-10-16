# from django.contrib.auth.models import User
from django.db import models


def ids(items):
    return map(lambda x: x.id, items.all())


class MyUser(models.Model):
    name = models.CharField(max_length=200)
    # user = models.OneToOneField(User, related_name="shekel")

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    customer = models.ForeignKey(MyUser, related_name="bought")
    consumers = models.ManyToManyField(MyUser, related_name="consumed")

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cost": self.cost,
            "customer": self.customer,
            "consumers_ids": ids(self.consumers)
        }

    def __str__(self):
        return self.name + "(" + str(self.cost) + ")"


class Purchase(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(MyUser)
    # party = models.ForeignKey(Event, related_name="purchases")

    cost = models.IntegerField()
    shared = models.ManyToManyField(MyUser, related_name="q")
    items = models.ManyToManyField(Item)

    def as_dict(self):
        return {
            "id": self.id,
            # "party_id": self.party_id,
            "name": self.name,
            "cost": self.cost,
            "items_ids": ids(self.items),
            "shared_ids": ids(self.shared)
        }

    def __str__(self):
        return self.name + "(" + str(self.cost) + ")"
