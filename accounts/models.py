from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from company.models import CompanyModel


class UserProfile(models.Model):
    objects = models.Manager()
    company = models.ForeignKey(CompanyModel, null=True,
                                                blank=True )
    user = models.ForeignKey(User)
    city = models.CharField(max_length=30)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username