from django.db import models

YEAR = (
    ('Second', 'Second'),
    ('Third', 'Third'),
    ('Fourth', 'Fourth'),
    ('NA', 'NA'),
)

class Member(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    #current_year = models.CharField(max_length=10, choices=YEAR, default='NA')
    passout_year = models.CharField(max_length=10, default='2017')
    post = models.CharField(max_length=100, null=True,blank=True, default='NA')
    dp = models.ImageField(upload_to='memberDPs/', blank=True, null=True)
    instagram_url = models.URLField(max_length=300, null=True, blank=True)
    linkedin_url = models.URLField(max_length=300, null=True, blank=True)
    facebook_url = models.URLField(max_length=300, null=True, blank=True)
    github_url = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.firstname
   
   



