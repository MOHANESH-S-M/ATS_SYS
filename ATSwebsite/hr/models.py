from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


# Create your models here
class jobpost(models.Model):
    hr = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.TextField()
    location = models.CharField(max_length=70)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,blank= True)

    def __str__(self):
        return self.title
    def save(self,*args ,**kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.hr.id}-{timezone.now().timestamp()}')
        super().save(*args,**kwargs)

    def is_expired(self):
        return self.deadline < timezone.now().date()
    