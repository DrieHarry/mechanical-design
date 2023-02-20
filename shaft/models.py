from django.db import models

# Create your models here.
class ResultType1(models.Model):
    d1 = models.FloatField()
    d2 = models.FloatField()
    d3 = models.FloatField()

    def __str__(self):
        return f"Hasil {self.id}: Da= {self.d1} Db= {self.d2} Dc= {self.d3}"