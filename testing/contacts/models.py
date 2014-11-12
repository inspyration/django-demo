from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=32)


class Contact(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    position = models.ForeignKey(Position)
    create_date = models.DateTimeField('date created')
