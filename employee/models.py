from django.db import models

# Create your models here.

class CustomerSupport(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    by_from = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=10)
    # profile = models.ImageField(upload_to="profile/employees/")
    description = models.TextField()
    solution = models.TextField()
    # docs = models.FileField(upload_to='employes/documents/')
    def __str__(self):
        return self.name
    

class messsanger(models.Model):
    name = models.CharField(max_length=225)
    msg = models.TextField()
    sender_id = models.CharField(max_length=11)
    sender_type = models.CharField(max_length=10)
    created = models.CharField(max_length=6)
     
    def __str__(self):
        return self.name