from email.policy import default
from re import U
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Event(models.Model):
    class Meta:
        db_table = 'Event'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=20, null=False)
    description = models.CharField(max_length=300, blank=True)
    credit = models.DecimalField(max_digits=14, decimal_places=4)
    task_datetime = models.DateTimeField(
        null=False, blank=False, default=datetime.datetime.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(help_text='income:0, expense:1', default=0)

    def __str__(self) -> str:

        return self.title
