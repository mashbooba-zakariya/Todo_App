from django.db import models
import datetime

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()

    # date_string = str(date)

    def __str__(self):
        return self.title + " , " + self.date.strftime("%Y-%m-%d")

