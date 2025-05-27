from django.db import models

# Create your models here
class job_post(models.Model):
    title = models.CharField(max_length=70)
    decscription = models.TextField()
    location = models.CharField(max_length=70)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title