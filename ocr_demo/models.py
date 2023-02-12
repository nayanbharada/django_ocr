from django.db import models

# Create your models here.


class NetworkData(models.Model):
    """
    this is table in network data is store
    """
    method_name = models.CharField(max_length=50)
    category_one = models.FloatField()
    category_two = models.FloatField()
    category_three = models.FloatField()
    category_four = models.FloatField()

    def __str__(self):
        return f"{self.method_name}"

