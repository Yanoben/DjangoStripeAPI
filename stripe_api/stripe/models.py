from django.db import models


class Item(models.Model):
    name = models.CharField()
    description = models.TextField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
