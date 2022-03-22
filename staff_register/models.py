from django.db import models

# Create your models here.
class Position(models.Model):
    title        = models.CharField(max_length = 50)

    def __str__(self):
        return self.title


class Staff(models.Model):
    fullname      = models.CharField(max_length = 100)
    staff_code    = models.CharField(max_length = 100)
    phone         = models.CharField(max_length = 11)
    position      = models.ForeignKey(Position,on_delete=models.CASCADE)
     

    
    