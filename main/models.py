import os
from datetime import datetime
from time import time

from accounts.models import User
from django.db import models
from tomlkit import comment


def upload_to(record, filename):
    extension = os.path.splitext(filename)[
        1
    ]  # gets the file extension from filename e.g .pdf, .csv, .xlsv
    return "records/{user_id}/{filename}{extension}".format(
        user_id=record.user.id,
        filename=str(datetime.now().timestamp()).replace(".", "_"),
        extension=extension,
    )


class CancerRecord(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    file = models.FileField(upload_to=upload_to, blank=False, null=False)
    upload_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    update_time = models.DateTimeField(auto_now=True, null=False, blank=False)


class Comment(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    record = models.ForeignKey(
        CancerRecord, null=False, blank=False, on_delete=models.CASCADE
    )
    comment = models.TextField(null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True, null=False, blank=False)
