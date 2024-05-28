from django.db import models


# University_list = (
#     ('SVUTPT' , "Sri Venkataswara University , Tirupati"),
#     ('APUVIZ' , "Andra University ,  Visakhapatnam"),
# )



Subjects_list = (
    ('PY' , "Python"),
    ('JAVA' , "Java"),
    ('C' , "C Lanaguage"),
    ('CPP' , "C++ Lanaguage"),
    ('DBMS' , "Data Base Manaagement System"),
    ('PHP' , "PHP"),
    ('HTML' , "HTML"),
    ('JS' , "Java Script"),
    ('R' , "R language"),
    ('C#' , "C hash"),
    ('GO' , "GO Lanaguage"),
    ('SWIFT' , "SWIFT Lanaguage"),
    ('RUST' , "RUST Lanaguage"),

)


class University(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    uni = models.CharField( max_length = 6)
    city = models.CharField(max_length=54)
    postal = models.CharField(max_length=254)
    profile = models.ImageField(upload_to="profile/university/")
    def __str__(self):
        return self.name
    

class Question(models.Model):
    problem = models.CharField(max_length=250)
    a = models.CharField(max_length=250)
    b = models.CharField(max_length=50)
    c = models.CharField( max_length = 250)
    d = models.CharField(max_length=250)
    ans = models.CharField(max_length=1)
    uni = models.CharField(max_length=6)
    clg  = models.CharField(max_length=10)
    sub = models.CharField(choices = Subjects_list , max_length = 5)
    def __str__(self):
        return self.problem