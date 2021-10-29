from django.db import models

# Create your models here.
class Club(models.Model):
    image = models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=200)

    def _str_(self):
        return self.summary