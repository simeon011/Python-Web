from django.db import models

from advertisement_center.choices import ProcessingStatus, VideoFormat
from advertisement_center.validators import video_validator


class Commercial(models.Model):
    slogan = models.CharField(max_length=100)
    body = models.TextField()
    video = models.FileField(upload_to='commercial/%Y/%m/%d/', validators=[video_validator])
    processing_status = models.CharField(choices=ProcessingStatus.choices, default=ProcessingStatus.Pending, max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    video_duration = models.PositiveIntegerField(default=0)
    video_format = models.CharField(max_length=10, choices=VideoFormat.choices, blank=True, default='')
    size_in_bytes = models.PositiveIntegerField(default=0)

