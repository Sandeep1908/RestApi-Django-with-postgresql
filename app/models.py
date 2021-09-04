from django.db import models

#This is the model class for student data adding into database table
class userdata(models.Model):
    name    = models.CharField(max_length=80)
    roll    = models.IntegerField()
    subject = models.CharField(max_length=80)

    def __str__(self):
        return self.name

