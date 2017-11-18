from django.db import models
from django.utils import timezone

class Load(models.Model):
    load_number = models.IntegerField()
    carrier = models.TextField()
    pickup_date = models.DateField()
    delivery_date = models.DateField()
    shipper = models.TextField()
    consignee = models.TextField()
    po_number = models.TextField()
    pu_number = models.TextField()
    pieces = models.IntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.date_created = timezone.now()
        self.save()

    def __str__(self):
        return str(self.load_number)