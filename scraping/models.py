from django.db import models


# Create your models here.
class Proxy(models.Model):
    ip = models.CharField(max_length=45, unique=True)
    port = models.IntegerField()
    protocol = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    anonymity = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    uptime = models.CharField(max_length=255)
    response = models.CharField(max_length=255)

    def __str__(self):
        return self.ip

    def save(self, *args, **kwargs):
        self.ip = self.ip.lower()
        self.uptime = self.uptime + "%"
        self.response = self.response + "%"
        super(Proxy, self).save(*args, **kwargs)
