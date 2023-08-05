from django.db import models

MODE = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),
)

class event(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField(max_length=50000)
    poster = models.ImageField(
        upload_to='eventPosters/', blank=True, null=True)
    event_datetime = models.DateTimeField(
        'Date of event : ', auto_now_add=False)
    event_mode = models.CharField(
        max_length=15, choices=MODE, default='Online')

    event_starttime = models.DateTimeField(
        "Start Date of the event: ", auto_now_add=False)
    event_endtime = models.DateTimeField(
        "End date of the event: ", auto_now_add=False)

    
    text1 = models.CharField(blank=True, max_length=20)
    url1 = models.CharField(blank=True, max_length=500)
    text2 = models.CharField(blank=True, max_length=20)
    url2 = models.CharField(blank=True, max_length=500)
    text3 = models.CharField(blank=True, max_length=20)
    url3 = models.CharField(blank=True, max_length=500)

    class Meta:
        ordering = ['-event_datetime']

    def __str__(self):
        return self.event_name
