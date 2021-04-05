from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

# Create your models here.
class Guess(models.Model):
    guess = models.CharField(max_length = 40)

#class Guess(models.Model):
   # guess = models.CharField(default = 'guess', max_length = 4)

class product(models.Model):
    title = models.TextField()
    description = models.TextField()
    summary = models.TextField(default = 'this is great')




    
 

