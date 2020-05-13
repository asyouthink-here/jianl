from django.db import models
from .views import cascade


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('e-mail', blank=True, null=True)
    age = models.CharField(max_length=2, blank=True, null=True)

    def __unicode__(self):
        return u'%s''%s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, verbose_name='programmer')
    publisher = models.ForeignKey(Publisher, on_delete=cascade, blank=True, null=True)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title
