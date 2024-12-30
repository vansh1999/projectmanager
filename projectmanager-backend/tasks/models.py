from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=160)

    def __str__(self):
        return self.name
