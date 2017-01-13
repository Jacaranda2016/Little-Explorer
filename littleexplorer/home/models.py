from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    category = models.ForeignKey('home.Category', null=True)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    thumb = models.CharField(max_length=200, null=True)
    summary = models.CharField(max_length=1000, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    shortUrl = models.CharField(max_length=200, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=60, blank=True)

    #Then override models save method:
    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.title) #Or whatever you want the slug to use
        super(Post, self).save(*args, **kwargs)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    thumb = models.CharField(max_length=200, null=True)
    summary = models.CharField(max_length=1000, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    shortUrl = models.CharField(max_length=200, null=True)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

