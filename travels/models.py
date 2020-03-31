from django.db import models


# Create your models here.

class Travel(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=50, blank=True, default="")
    place = models.CharField(max_length=50)
    notes = models.CharField(max_length=100)
    owner = models.ForeignKey("auth.User", related_name="travels",
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']
