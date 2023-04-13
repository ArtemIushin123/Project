from django.db import models


class Client(models.Model):
    name = models.CharField('Name,', max_length=30)
    telephone = models.CharField('Telephone', max_length=12)
    mail = models.CharField('Mail', max_length=30)

    def __str__(self):
        return self.name

