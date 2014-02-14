from django.db import models

# Create your models here.


class Article(models.Model):
    publish_date = models.DateTimeField('date published')
    publisher= models.CharField(max_length=200)
    content = models.TextField()
    snippet = models.TextField()
    title=models.CharField(max_length=400)
    
    def __unicode__(self):
        return self.title

