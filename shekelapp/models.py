from django.contrib.auth.models import User
from django.db import models


def ids(items):
    return list(map(lambda x: x.id, items.all()))


class MyUser(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, default=1, related_name="shekel")

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    # receipt = models.ForeignKey(Receipt, related_name='bought_in')
    cost = models.IntegerField()
    customer = models.ForeignKey(MyUser, related_name='bought')
    consumers = models.ManyToManyField(MyUser, related_name='consumed')

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cost': self.cost,
            'customer': self.customer.id,
            'consumer_ids': ids(self.consumers)
        }

    def fill(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name + "(" + str(self.cost) + ")"


class Receipt(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(MyUser, related_name="receipts")
    # party = models.ForeignKey(Event, related_name="purchases")
    cost = models.IntegerField()
    shared = models.ManyToManyField(MyUser, related_name="q")
    items = models.ManyToManyField(Item, related_name="contained_by")

    def as_dict(self):
        return {
            'id': self.id,
            # "party_id": self.party_id,
            'name': self.name,
            'owner': self.owner.id,
            'cost': self.cost,
            'items': list(map(lambda x: x.as_dict(), self.items.all())),
            'consumer_ids': ids(self.shared),
            # 'consumers': list(map(lambda x: x.as_dict(), self.shared.all()))
            # 'items_ids': ids(self.items),
        }

    def __str__(self):
        return self.name + "(" + str(self.cost) + ")"




