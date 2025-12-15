from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_score(self):
        return self.q1 + self.q2 + self.q3 + self.q4 + self.q5

    @property
    def average_score(self):
        return self.total_score / 5
