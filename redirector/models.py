from django.db import models


class Email(models.Model):
    email_value = models.EmailField()
    goto_url = models.URLField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
