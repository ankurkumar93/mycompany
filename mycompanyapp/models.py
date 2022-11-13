from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    contactNumber = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Inquirie'