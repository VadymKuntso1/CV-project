from django.db import models

class WordLan(models.Model):
    id = models.IntegerField('id', primary_key=True, auto_created=True)
    eng = models.CharField('word', max_length=1000)
    ua = models.CharField('word', max_length=1000)

    def __str__(self):
        return self.eng + ' ' + self.ua

class Words:
    contact = ''
    Experience = ''
    exp1 = ''
    aboutme=''
    ab1=''
    Education=''
    edt=''
    ed1=''
    ed2=''
    Skills=''
    sk1=''
    sk2=''
    sk3=''
    sk4=''
    Stack=''
    age=''
    lang = ''