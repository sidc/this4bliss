from django.db import models

# Create your models here.

class Soul(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True, unique=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    event = models.TextField(null=True, blank=True)
    date = models.DateField('distributed',null=True, blank=True)
    book = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    distributor = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name