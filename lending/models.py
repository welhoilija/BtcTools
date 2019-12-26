from django.db import models

# Create your models here.



class lending(models.Model):

    """
    Lending model
    """
    amount = models.CharField(max_length=20)
    payday = models.DateTimeField("pay date")
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.lending_text

    class Meta:
        pass