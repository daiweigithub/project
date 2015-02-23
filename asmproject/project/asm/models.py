from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created_date',)

class Record(BaseModel):
    owner = models.ForeignKey('auth.User', related_name='records', on_delete=models.CASCADE)
    recordType = models.IntegerField(default=0)
    organ = models.CharField(max_length=16, default='')
    udata = models.FloatField(default=0)
    peakFlow = models.FloatField(default=0)
    fev1 = models.FloatField(default=0)

