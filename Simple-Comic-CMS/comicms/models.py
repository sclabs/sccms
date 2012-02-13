from django.db import models

# Create your models here.
class Comic(models.Model):
    number = models.IntegerField(primary_key = True)
    img_src = models.FileField(upload_to = 'comics')
    title = models.CharField(max_length = 200)
    tooltip = models.TextField()
    date = models.DateField()
    
    def __unicode__(self):
        return self.title