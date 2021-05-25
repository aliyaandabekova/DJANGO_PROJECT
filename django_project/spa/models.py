from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=40, unique=True)
    price = models.IntegerField()
    master = models.ForeignKey("Master", on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class Master(models.Model):
    photo = models.ImageField()
    full_name = models.CharField(max_length=30)
    exp = models.IntegerField(default=0)
    birth_date = models.DateField()




