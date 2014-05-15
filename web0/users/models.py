from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    message_box = models.ForeignKey('content.Item')
    mentor_user = models.ForeignKey('User', null=True, blank=True)

    def __unicode__(self):
        return self.name
