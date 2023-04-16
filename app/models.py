from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=20,primary_key=True)
    def __str__(self) -> str:
        return self.Topic_name

class Webpages(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    URL=models.URLField()
    Email=models.EmailField()
    def __str__(self) -> str:
        return self.Name
class AccessRecord(models.Model):
    Name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    Auther=models.CharField(max_length=20)
    DOB=models.DateField()
    Country=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.Auther
