from django.db import models


# Create your models here.
class Materials(models.Model):
    SAE_Number = models.CharField(max_length=64)
    tegangan_tarik = models.FloatField()
    tegangan_luluh = models.FloatField()

    def __str__(self):
        return f"{self.SAE_Number}: Su = {self.tegangan_tarik} MPa; Sy = {self.tegangan_luluh} MPa"


class ResultType1(models.Model):
    d1 = models.FloatField()
    d2 = models.FloatField()
    d3 = models.FloatField()

    def __str__(self):
        return f"Hasil {self.id}: Da= {self.d1} Db= {self.d2} Dc= {self.d3}"
