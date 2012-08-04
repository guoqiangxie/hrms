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

class Employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    telephone = models.CharField(max_length=20)
    level = models.CharField(max_length=10)

    def __unicode__(self):
            return self.name

class Overtimeform(models.Model):
    begintime = models.DateTimeField()
    endtime = models.DateTimeField()
    reason = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    applyer = models.ForeignKey(Employee)
    status = models.CharField(max_length=5)

    def __unicode__(self):
        return self.applyer + self.reason

class Employee_overtimeform_ref(models.Model):
    employee = models.ForeignKey(Employee)
    overtimeform = models.ForeignKey(Overtimeform)

    def __unicode__(self):
        return self.employee + self.overtimeform


class apply_track(models.Model):
    overtimeform = models.ForeignKey(Employee_overtimeform_ref)
    approval = models.ForeignKey(Employee)
    approval_note = models.CharField(max_length=255)
    apply_date = models.DateTimeField()
    type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.approval + self.overtimeform + self.type