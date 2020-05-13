from django.db import models
from .views import CASCADE


class Basic(models.Model):
    name = models.CharField(max_length=10)
    birth = models.DateField()
    phonenumber = models.CharField(max_length=30, blank=True, null=True)
    Email = models.EmailField('e-mail', blank=True, null=True)
    job = models.CharField(max_length=10)
    # idcard = models.CharField(max_length=20)
    native = models.CharField(max_length=30)
    politic = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Education(models.Model):
    education = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    rank = models.CharField(max_length=30)
    intake = models.CharField(max_length=30)
    graduation_time = models.DateField()

    def __unicode__(self):
        return self.graduation_time


class Procedules(models.Model):
    time_on = models.DateField()
    time_off = models.DateField()
    achievements = models.CharField(max_length=100)
    position = models.CharField(max_length=20)


class Schooltime(models.Model):
    association = models.CharField(max_length=30)
    procedules = models.ForeignKey(Procedules, on_delete=CASCADE, blank=True, null=True)


class Workexperience(models.Model):
    corporation = models.CharField(max_length=30)
    procedules = models.ForeignKey(Procedules, on_delete=CASCADE,  blank=True, null=True)

    def __unicode__(self):
        return self.procedules


class Project(models.Model):
    corporation = models.CharField(max_length=30)
    procedules = models.ForeignKey(Procedules, on_delete=CASCADE, blank=True, null=True)


class Rewarded(models.Model):
    prize = models.CharField(max_length=20)
    winningtime = models.DateField()


class Text(models.Model):
    skills = models.TextField(max_length=200)
    selfassessment = models.TextField(max_length=200)
    sublication = models.TextField(max_length=200)

    def __unicode__(self):
        return self.skills


class Jobintansion(models.Model):
    address = models.CharField(max_length=20)
    postion = models.CharField(max_length=20)

    def __unicode__(self):
        return self.address
