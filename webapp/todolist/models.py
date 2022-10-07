from django.db import models
class User(models.Model):
    id = models.IntegerField('id',primary_key=True,auto_created=True)
    login = models.CharField('Login',max_length=20, unique=True)
    password = models.CharField('Password',max_length=50)

    def __str__(self):
        return 'Login:'+self.login+'\nPassword:'+self.password