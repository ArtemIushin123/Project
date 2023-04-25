from django.db import models


class Client(models.Model):
    name = models.CharField('Name,', max_length=30)
    telephone = models.CharField('Telephone', max_length=12)
    mail = models.EmailField('Mail', max_length=30)
    client_city = models.CharField('Client_city', max_length=30)

    def __str__(self):
        return self.name

