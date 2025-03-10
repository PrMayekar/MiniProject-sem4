from django.db import models

class WeatherData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather at ({self.latitude}, {self.longitude}): {self.temperature}°C, {self.description}"
