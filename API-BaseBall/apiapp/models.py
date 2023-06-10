from django.db import models

class Baseball(models.Model):
    name = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + ' | ' + self.division + ' | ' + str(self.city)