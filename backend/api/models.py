from django.db import models

# Create your models here.


class IndeedJobs(models.Model):
    title = models.CharField(max_length=500)
    job_url = models.CharField(max_length=500)
    job_id = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    salary = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
