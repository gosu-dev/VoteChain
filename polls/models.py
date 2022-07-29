from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.


class Poll(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # date_start = models.DateTimeField()
    # date_end = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.option[0:50]}'


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll_option = models.ForeignKey(PollOption, on_delete=models.CASCADE)
