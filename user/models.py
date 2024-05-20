from django.db import models


University_list = (
    ('SVUTPT' , "Sri Venkataswara University , Tirupati"),
    ('APUVIZ' , "Andra University ,  Visakhapatnam"),
)


class Student(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    hall_no = models.CharField(max_length=50)
    college = models.CharField(max_length=254)
    clg_code = models.CharField(max_length=10)
    university = models.CharField(choices = University_list , max_length = 6)
    profile = models.ImageField(upload_to="profile/students/")
    terms =  models.CharField(max_length=6)
    user_name =  models.CharField(max_length=60)
    

    def __str__(self):
        return self.name
