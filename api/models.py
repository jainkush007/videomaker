from django.db import models


class AudioBlock(models.Model):
    AUDIO_TYPES = (
        ('vo', 'Voice Over'),
        ('bg_music', 'Background Music'),
        ('video_music', 'Video Music'),
    )

    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=20, choices=AUDIO_TYPES)
    high_volume = models.IntegerField()
    low_volume = models.IntegerField()
    video_component_id = models.ForeignKey('VideoBlock', on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    duration_start_time = models.DurationField(null=True, blank=True)
    duration_end_time = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.id


class VideoBlock(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=20)
    audio_id = models.OneToOneField(AudioBlock, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField()
    duration_start_time = models.IntegerField()
    duration_end_time = models.IntegerField()

    def __str__(self):
        return self.id


class Project(models.Model):
    audio_blocks = models.ManyToManyField(AudioBlock)
    video_blocks = models.ManyToManyField(VideoBlock)

    def __str__(self):
        return f"Project {self.id}"
