from django.db import models

# Create your models here.
class contactus(models.Model):
    name=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=40,null=True)
    massage=models.TextField(null=True)
    

class igallery(models.Model):
    picture=models.ImageField(upload_to="static/gallery/",null=True)    
    title=models.CharField(max_length=30,null=True)    


class ourplacement(models.Model):
    name=models.CharField(max_length=50,null=True)    
    picture=models.ImageField(upload_to="static/placement",null=True)
    psession=models.CharField(max_length=20,null=True)
    company=models.CharField(max_length=40,null=True)
    branch=models.CharField(max_length=50,null=True)

class mycourse(models.Model):
    branch=models.CharField(max_length=40,null=True)
    picture=models.ImageField(upload_to="static/branch/",null=True)
    seats=models.CharField(max_length=50,null=True)

class ourfaculty(models.Model):
    name=models.CharField(max_length=50,null=True)
    picture=models.ImageField(upload_to="static/faculty",null=True)
    qualification=models.CharField(max_length=40,null=True)
    experience=models.CharField(max_length=40,null=True)
    fposts=models.CharField(max_length=80,null=True)


class myfacilities(models.Model):
    name=models.CharField(max_length=40,null=True)
    picture=models.ImageField(upload_to="static/branch/",null=True)
    
class notice(models.Model):
    name=models.CharField(max_length=200,null=True)
    
