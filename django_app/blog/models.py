from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1222)
    body = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title
