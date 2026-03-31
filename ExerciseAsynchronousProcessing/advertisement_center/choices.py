from django.db import models


class ProcessingStatus(models.TextChoices):
    PROCESSING = 'processing', 'Processing',
    Pending = 'pending', 'Pending',
    Completed = 'completed', 'Completed',
    Failed = 'failed', 'Failed',


class VideoFormat(models.TextChoices):
    MP4 = 'mp4', 'MP4',
    MOV = 'mov', 'MOV',
    MKV = 'mkv', 'MKV',
