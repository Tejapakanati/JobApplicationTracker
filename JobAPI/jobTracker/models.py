from django.db import models

class JobApplication(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_id = models.CharField(max_length=100,blank=True)
    location = models.CharField(max_length=100, blank=True)
    application_date = models.DateField(blank=True)
    status = models.CharField(max_length=100)
    job_url = models.URLField(blank=True)
    source = models.CharField(blank=True)
    notes = models.CharField(blank=True)

    def __str__(self) :
        return f"{self.company} - {self.job_title}"
