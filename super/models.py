from django.db import models
# Create your models here.


roles = (
    ('Coustomer Support' , "Coustomer Support"),
    ('Python developer' , "Python developer"),
)
class Employ(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    role = models.CharField(choices = roles ,max_length = 50)
    emp_id = models.CharField(max_length=10)
    profile = models.ImageField(upload_to="profile/employees/")
    designation =  models.CharField(max_length=6)
    description = models.CharField(max_length=5000)
    # docs = models.FileField(upload_to='employes/documents/')
    def __str__(self):
        return self.name