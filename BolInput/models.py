from django.db import models
from django.utils import timezone


class Load(models.Model):
    load_number = models.IntegerField()
    carrier = models.CharField(max_length=True)
    pickup_date = models.DateField()
    delivery_date = models.DateField()
    shipper = models.CharField(max_length=True)
    consignee = models.CharField(max_length=True)
    po_number = models.CharField(max_length=True)
    pu_number = models.CharField(max_length=True)
    pieces = models.IntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.date_created = timezone.now()
        self.save()

    def __str__(self):
        return str(self.load_number)