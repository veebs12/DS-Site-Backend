from django.db import models
YEAR = (
    ('Second', 'Second'),
    ('Third', 'Third'),
    ('Fourth', 'Fourth'),
)

class Members(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, null=True, blank=True)
    year = models.CharField(max_length=10, choices=YEAR, default='Second')
    post = models.CharField(max_length=100, null=True,
                            blank=True, default='Senior Member')
    dp = models.ImageField(upload_to='memberDPs/', blank=True, null=True)
    instagram_url = models.URLField(max_length=300, null=True, blank=True)
    linkedin_url = models.URLField(max_length=300, null=True, blank=True)
    facebook_url = models.URLField(max_length=300, null=True, blank=True)
    github_url = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.firstname


class Alumni(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(max_length=254, null=True, blank=True)
    passout_year = models.CharField(max_length=10, default='2017')
    dp = models.ImageField(upload_to='alumniDPs/', blank=True, null=True)
    facebook_url = models.URLField(max_length=300, null=True, blank=True)
    instagram_url = models.URLField(max_length=300, null=True, blank=True)
    linkedin_url = models.URLField(max_length=300, null=True, blank=True)
    github_url = models.URLField(max_length=300, null=True, blank=True)



