from django.db import models

# Create your models here.
class cv(models.Model):
    name=models.CharField(max_length=40)
    address=models.TextField(max_length=200)
    phone=models.IntegerField()
    email=models.CharField(max_length=40)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')

    def __str__(self):
        return self.name

class Career(models.Model):
    title            = models.CharField(max_length=30)
    Career_Objective = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class Education(models.Model):
    title=models.CharField(max_length=50)
    Bachelor_of_Science    =models.CharField(max_length=50)
    Institutionu           =models.CharField(max_length=50)
    session = models.IntegerField()
    HSC                    =models.CharField(max_length=50,blank=True)
    Backgroundh = models.CharField(max_length=50)
    Institutionh           =models.CharField(max_length=50)
    Boardh    =models.CharField(max_length=50)
    resulth    =models.IntegerField()
    passingyearh    =models.IntegerField()
    SSC                    =models.CharField(max_length=50,blank=True)
    Backgrounds    =models.CharField(max_length=50)
    Institutions    =models.CharField(max_length=50)
    Boards    =models.CharField(max_length=50)
    results    =models.IntegerField()
    passingyears    =models.IntegerField()

    def __str__(self):
        return self.title



class Programming(models.Model):
    title=models.CharField(max_length=50)
    python=models.CharField(max_length=50)
    android=models.CharField(max_length=50)
    c=models.CharField(max_length=50)
    html=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Language(models.Model):
    title=models.CharField(max_length=50)
    english=models.CharField(max_length=100)
    expert=models.CharField(max_length=100)
    word=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class projects(models.Model):
    title=models.CharField(max_length=30)
    project1=models.CharField(max_length=30)
    project2=models.CharField(max_length=30)
    project3=models.CharField(max_length=30)
    project4=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class personal(models.Model):
    title=models.CharField(max_length=30)
    father=models.CharField(max_length=30)
    mother=models.CharField(max_length=30)
    nationality=models.CharField(max_length=30)
    religion=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    height=models.IntegerField()

    def __str__(self):
        return self.title



