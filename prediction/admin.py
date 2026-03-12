from django.contrib import admin
from .models import JobPrediction


@admin.register(JobPrediction)
class JobPredictionAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'prediction_type', 'automation_probability', 'risk_category', 'created_at']
    list_filter = ['prediction_type', 'risk_category']
    search_fields = ['job_title']

