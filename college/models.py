from django.db import models


University_list = (
    ('SVUTPT' , "Sri Venkataswara University , Tirupati"),
    ('APUVIZ' , "Andra University ,  Visakhapatnam"),
)


# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    university = models.CharField(choices = University_list , max_length = 6)
    clg_code = models.CharField(max_length=10)
    city = models.CharField(max_length=54)
    postal = models.CharField(max_length=254)
    profile = models.ImageField(upload_to="profile/college/")
    terms =  models.CharField(max_length=6)
    principal =  models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Python(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class Java(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class Clang(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class CPPlang(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class Chash(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
        
class HTML(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name

class JavaScript(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name

class Rlang(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class GOlang(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class SWIFT(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class RUST(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class DBMS(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name
    
class PHP(models.Model):
    name = models.CharField(max_length=50)
    user_id  = models.CharField(max_length=12)
    test = models.IntegerField()
    payment = models.CharField( max_length = 50)
    time = models.DateTimeField()
    pay_time = models.DateTimeField()
    test_time = models.DateTimeField()
    test_due = models.DateTimeField()
    def __str__(self):
        return self.name