from django.db import models

# Create your models here.



class lending(models.Model):

    """
    Lending model
    """
    amount = models.CharField(max_length=20)
    payday = models.DateTimeField("pay date")
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.amount + " " + self.email

    class Meta:
        pass