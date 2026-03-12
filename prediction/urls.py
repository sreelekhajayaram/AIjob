"""
URL Configuration for Prediction App
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict_slr', views.predict_slr, name='predict_slr'),
    path('predict_mlr', views.predict_mlr, name='predict_mlr'),
    path('predict_logistic', views.predict_logistic, name='predict_logistic'),
    path('predict_knn', views.predict_knn, name='predict_knn'),
    path('predict_polynomial', views.predict_polynomial, name='predict_polynomial'),
]

