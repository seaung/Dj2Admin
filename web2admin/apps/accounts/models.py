from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    GENDER_CHOICES = (
            ('M', 'male'),
            ('F', 'famale')
        )
    name = models.CharField(verbose_name='name', null=True, blank=True, max_length=50)
    age = models.IntegerField(verbose_name='age', null=True, blank=True, default=0)
    birthday = models.DateField(verbose_name='birthday', null=True, blank=True)
    gender = models.CharField(verbose_name='gender', choices=GENDER_CHOICES, default='manle', max_length=10)
    mobile = models.CharField(verbose_name='mobile', null=True, blank=True, max_length=11)
    email = models.EmailField(verbose_name='email', null=True, blank=True, max_length=100)
    join_date = models.DateTimeField(verbose_name='join date', null=True, blank=True, default=datetime.now)

    class Meta:
        verbose_name = 'users'
        verbose_name_plural = verbose_name

        app_label = 'accounts'
        db_table = 'users'

    def __str__(self):
        return self.name


class VerfyCode(models.Model):
    email = models.EmailField(verbose_name='email', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='code', null=True, blank=True, max_length=16)
    add_time = models.DateTimeField(verbose_name='add time', null=True, blank=True, default=datetime.now)

    class Meta:
        app_label = 'accounts'
        db_table = 'code'

    def __str__(self):
        return self.code

