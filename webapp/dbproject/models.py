from django.db import models

class Table(models.Model):
    id = models.IntegerField('id', primary_key=True, auto_created=True)
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name

class WordL(models.Model):
    id = models.IntegerField('id', primary_key=True, auto_created=True)
    eng = models.CharField('word', max_length=1000)
    ua = models.CharField('word', max_length=1000)

    def __str__(self):
        return self.eng + ' ' + self.ua