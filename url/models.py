from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_url(value):
    if not 'localhost' in value:
        raise ValidationError('Url is incorrect')
    return value

class UrlModel(models.Model):
    url = models.URLField(max_length=300,)
    slug = models.SlugField(unique=True)
    counter = models.IntegerField(default=0)
    def __str__(self):
        return self.url


    
class ReportLinkModel(models.Model):
    url = models.CharField(max_length=300, validators=[validate_url])
    comment = models.TextField()
    created_at = models.DateTimeField('Yuborilgan vaqti',auto_now_add=True, null=True)

    def __str__(self):
        return self.url 



class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField('Yuborilgan vaqti',auto_now_add=True, null=True)

    def __str__(self):
        return self.name