from django.db import models
from django.utils import timezone
from hr.models import jobpost

# Create your models here.

class Application(models.Model):
    CHOICES = [("sortlisted","Sortlisted"),("pending","Pending"),("rejected","Rejected"),]
    job = models.ForeignKey(jobpost,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    coverletter = models.TextField(blank=True ,null= True)
    applied_at = models.DateTimeField(default=timezone.now)

    ats_score = models.FloatField(null=True,blank=True)
    status = models.CharField(max_length=20,choices=CHOICES,default="pending")
    
    def __str__(self):
        return f"{self.fullname} applied for {self.job.title}"