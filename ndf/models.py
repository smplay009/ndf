from django.db import models

class Rating(models.Model):
    answers = models.JSONField("پاسخ سوالات")  
    total_score = models.PositiveSmallIntegerField("جمع امتیاز", editable=False)
    average_score = models.FloatField("میانگین امتیاز", editable=False)
    created_at = models.DateTimeField("تاریخ ثبت", auto_now_add=True)

    def save(self, *args, **kwargs):
        scores = list(self.answers.values())
        self.total_score = sum(scores)
        self.average_score = round(self.total_score / len(scores), 2) if scores else 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"⭐ {self.average_score}"
