from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    position = models.ForeignKey(Position)
    create_date = models.DateTimeField('date created')

    def __str__(self):
        return "{self.first_name} {self.last_name} ({self.position})".format(self=self)
