from django.db import models


class Client(models.Model):
    name = models.CharField('Name,', max_length=30)
    age = models.IntegerField('Age')
    birth_date = models.DateField('Birth Date')
    mail = models.CharField('Mail', max_length=30)

    def __str__(self):
        return self.name

