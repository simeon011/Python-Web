import math
from pathlib import Path

from django.core.exceptions import ValidationError
from django.db.models.query import ValuesListIterable

from advertisement_center.choices import VideoFormat

VIDEO_SIZE_LIMITS = {
    VideoFormat.MP4: 100,
    VideoFormat.MOV: 150,
    VideoFormat.MKV: 250
}


def video_validator(file):
    if not file:
        return

    extension = Path(file).suffix.lower().lstrip('.')
    if extension not in VIDEO_SIZE_LIMITS:
        supported_formats = ', '.join(choice.value for choice in VideoFormat)
        raise ValidationError(f"Unsupported video format. Supported formats: {supported_formats}")

    size_in_bytes = math.ceil(file.size / (1024 * 1024)) if file.size else 0
    allowed_size = VIDEO_SIZE_LIMITS[extension]

    if size_in_bytes > allowed_size:
        raise ValidationError(f"Video file size exceeds {allowed_size} MB")
