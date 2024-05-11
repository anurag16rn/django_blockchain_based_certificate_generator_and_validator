from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    name = models.CharField(max_length=100) 
    date = models.DateField()
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE)
    certificate = models.FileField(upload_to='certificates')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.certificate.name
    
class Report(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    issue = models.TextField()
    certificate_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

