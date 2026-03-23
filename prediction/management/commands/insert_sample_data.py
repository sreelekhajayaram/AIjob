from django.core.management.base import BaseCommand
from prediction.models import JobPrediction
import random
from datetime import datetime

class Command(BaseCommand):
    help = 'Insert sample JobPrediction records'

    def handle(self, *args, **options):
        # Sample data
        sample_jobs = [
            {
                'job_title': 'Software Engineer',
                'ai_exposure_index': 0.85,
                'tech_growth_factor': 0.92,
                'years_experience': 5.0,
                'average_salary': 120000.0,
                'automation_probability': 0.25,
                'risk_category': 'Low',
                'prediction_type': 'Full Analysis'
            },
            {
                'job_title': 'Data Scientist',
                'ai_exposure_index': 0.95,
                'tech_growth_factor': 0.98,
                'years_experience': 4.0,
                'average_salary': 140000.0,
                'automation_probability': 0.15,
                'risk_category': 'Very Low',
                'prediction_type': 'Full Analysis'
            },
            {
                'job_title': 'Customer Service Rep',
                'ai_exposure_index': 0.60,
                'tech_growth_factor': 0.45,
                'years_experience': 3.0,
                'average_salary': 45000.0,
                'automation_probability': 0.75,
                'risk_category': 'High',
                'prediction_type': 'Full Analysis'
            },
            {
                'job_title': 'Machine Learning Engineer',
                'ai_exposure_index': 0.98,
                'tech_growth_factor': 1.0,
                'years_experience': 6.0,
                'average_salary': 160000.0,
                'automation_probability': 0.08,
                'risk_category': 'Very Low',
                'prediction_type': 'Full Analysis'
            },
            {
                'job_title': 'Telemarketer',
                'ai_exposure_index': 0.40,
                'tech_growth_factor': 0.20,
                'years_experience': 2.0,
                'average_salary': 35000.0,
                'automation_probability': 0.90,
                'risk_category': 'Very High',
                'prediction_type': 'Full Analysis'
            },
        ]

        created = 0
        for data in sample_jobs:
            JobPrediction.objects.get_or_create(job_title=data['job_title'], defaults=data)
            created += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully inserted/updated {created} sample records')
        )

