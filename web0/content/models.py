from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=400)
    publish_date = models.DateTimeField('published',null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag,null=True, blank=True)
    CATEGORY_TYPES = (
        ('a','association'),
        ('b','book'),
        ('c','chanting'),
        ('d','diet')
    )
    category_type = models.CharField(max_length=4, choices=CATEGORY_TYPES,null=True, blank=True)
    ITEM_TYPES = (
        ('pdf','pdf'),
        ('audio','audio'),
        ('video','video'),
        ('article','article'),
        ('comment','comment'),
        ('mbox','message_box'),
        ('tag','tag')
    )
    item_type =  models.CharField(max_length=7, choices=ITEM_TYPES, null=True, blank=True)
    karma = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    dwnld = models.URLField(null=True, blank=True)
    approval = models.NullBooleanField(null=True, blank=True)
    related_item = models.ForeignKey('self',null=True, blank=True)
    publisher = models.ForeignKey('users.User',null=True, blank=True)
    
    def __unicode__(self):
        return self.title



    