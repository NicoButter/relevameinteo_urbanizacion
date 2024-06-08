from django.db import models

class Street(models.Model):
    name = models.CharField(max_length=100)
    start_number = models.IntegerField()
    end_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.start_number} - {self.end_number})"
