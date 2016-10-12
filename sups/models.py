from django.db import models

class Sup(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return self.text