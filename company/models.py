from django.db import models


class CompanyModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


