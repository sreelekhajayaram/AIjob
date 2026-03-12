from django.db import models


class JobPrediction(models.Model):
    """Model for storing job predictions"""
    job_title = models.CharField(max_length=200)
    ai_exposure_index = models.FloatField()
    tech_growth_factor = models.FloatField()
    years_experience = models.FloatField()
    average_salary = models.FloatField()
    automation_probability = models.FloatField(null=True, blank=True)
    risk_category = models.CharField(max_length=20, null=True, blank=True)
    prediction_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} - {self.prediction_type}"

