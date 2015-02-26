from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created_date',)

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename

class Record(BaseModel):
    owners = models.ManyToManyField(User, through='UserRecord')

    #path = models.FileField(upload_to=get_file_path)
    path = models.FileField(blank=True, default='')

    recordType = models.IntegerField(default=0)
    organ = models.CharField(max_length=16, default='')
    udata = models.FloatField(default=0)
    peakFlow = models.FloatField(default=0)
    fev1 = models.FloatField(default=0)
 
class UserRecord(BaseModel):
    owner = models.ForeignKey(User, related_name='userrecords', on_delete=models.CASCADE)
    record = models.ForeignKey(Record, related_name='userrecords', on_delete=models.CASCADE)
    relation = models.CharField( max_length=10, default='own' )

    def __unicode__(self):
        return " ".join([
           str(self.owner),
           str(self.record),
           str(self.relation),
        ])

