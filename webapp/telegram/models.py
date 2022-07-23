from django.db import models

class Profile(models.Model):
    id = models.IntegerField( verbose_name='User id', primary_key=True, auto_created=True)
    name = models.TextField( verbose_name='Nickname of user')
    class Meta:
        verbose_name = 'Telegram'
        verbose_name_plural = 'Telegram profiles'
    def __str__(self):
        return f'{self.id} {self.name}'

class Message(models.Model):
    profile = models.ForeignKey(to = 'telegram.Profile', verbose_name='Profile', on_delete=models.PROTECT,)
    text = models.TextField(verbose_name='Text')
    created_at = models.DateTimeField(verbose_name='Time of created', auto_now_add=True,)
    def __str__(self):
        return f'Profile: {self.pk} in {self.created_at}'
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
