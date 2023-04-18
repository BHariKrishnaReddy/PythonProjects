from django.db import models
from django.contrib.auth.models import User


# Create your models here. this is database. class is like a table and attributes are like features.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=225)
    desciprtion = models.TextField(null=True,blank=True)
    inProgress = models.BooleanField(default=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
