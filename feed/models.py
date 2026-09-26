from django.db import models

# Create your models here.
class Post(models.Model):
    #certain number of characters
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True) # y m d h m s but datefield just day
    def __str__(self):
        return self.text[0:100]    
