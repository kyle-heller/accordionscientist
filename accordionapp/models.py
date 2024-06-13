from django.db import models


class AccordionChart(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    layout = models.TextField()

    def __str__(self):
        return self.name
