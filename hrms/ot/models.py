from django.db import models

class Application(models.Model):
    subject = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    applicationDate = models.DateField()
    applicant = models.CharField(max_length=10)

    def __unicode__(self):
        return self.subject
    
class Person(models.Model):
    app = models.ForeignKey(Application)
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
