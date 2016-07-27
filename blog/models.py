from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    description = models.TextField()
    csdn = models.CharField(max_length=64)
    github = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class DownloadCategory(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Download(models.Model):
    name = models.CharField(max_length=64)
    time = models.DateField()
    filepath = models.CharField(max_length=64)
    category = models.ForeignKey(DownloadCategory, default='IT')

    def __unicode__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    abstract = models.TextField()
    created_time = models.DateTimeField()
    author = models.ForeignKey(Author, default="other")
    category = models.ForeignKey(BlogCategory, default='IT')

    def __unicode__(self):
        return self.title






