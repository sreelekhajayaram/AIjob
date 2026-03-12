"""
Django Views - Prediction Endpoints
"""
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .ml_utils import (
    simple_linear_regression,
    multiple_linear_regression,
    logistic_regression,
    knn_classification,
    polynomial_regression
)


@require_http_methods(["GET"])
def index(request):
    """Render the main dashboard page"""
    from django.shortcuts import render
    return render(request, 'index.html')


@csrf_exempt
@require_http_methods(["POST"])
def predict_slr(request):
    """
    Simple Linear Regression Prediction
    Predict Average Salary using Years Experience
    
    Endpoint: /predict_slr
    Input: {"years_experience": float}
    Output: {"prediction": dict with "annual" and "monthly", "model": "Simple Linear Regression"}
    """
    try:
        data = json.loads(request.body)
        years_experience = float(data.get('years_experience', 0))
        
        # Validate input
        if years_experience < 0:
            return JsonResponse({
                'error': 'Years Experience must be positive'
            }, status=400)
        
        prediction = simple_linear_regression(years_experience)
        
        return JsonResponse({
            'prediction': prediction,
            'model': 'Simple Linear Regression',
            'input': {'years_experience': years_experience}
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def predict_mlr(request):
    """
    Multiple Linear Regression Prediction
    Predict Automation Probability using:
    - AI Exposure Index
    - Tech Growth Factor
    - Years Experience
    - Average Salary
    
    Endpoint: /predict_mlr
    """
    try:
        data = json.loads(request.body)
        ai_exposure_index = float(data.get('ai_exposure_index', 0))
        tech_growth_factor = float(data.get('tech_growth_factor', 1.0))
        years_experience = float(data.get('years_experience', 0))
        average_salary = float(data.get('average_salary', 50000))
        
        # Validate inputs
        if not (0 <= ai_exposure_index <= 1):
            return JsonResponse({
                'error': 'AI Exposure Index must be between 0 and 1'
            }, status=400)
        
        if not (0.5 <= tech_growth_factor <= 1.5):
            return JsonResponse({
                'error': 'Tech Growth Factor must be between 0.5 and 1.5'
            }, status=400)
        
        if years_experience < 0:
            return JsonResponse({
                'error': 'Years Experience must be positive'
            }, status=400)
        
        if average_salary < 0:
            return JsonResponse({
                'error': 'Average Salary must be positive'
            }, status=400)
        
        prediction = multiple_linear_regression(
            ai_exposure_index,
            tech_growth_factor,
            years_experience,
            average_salary
        )
        
        return JsonResponse({
            'prediction': prediction,
            'model': 'Multiple Linear Regression',
            'input': {
                'ai_exposure_index': ai_exposure_index,
                'tech_growth_factor': tech_growth_factor,
                'years_experience': years_experience,
                'average_salary': average_salary
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def predict_logistic(request):
    """
    Logistic Regression Prediction
    Predict Risk Category (Low / Medium / High) using:
    - AI Exposure Index
    - Tech Growth Factor
    - Years Experience
    
    Endpoint: /predict_logistic
    """
    try:
        data = json.loads(request.body)
        ai_exposure_index = float(data.get('ai_exposure_index', 0))
        tech_growth_factor = float(data.get('tech_growth_factor', 1.0))
        years_experience = float(data.get('years_experience', 0))
        
        # Validate inputs
        if not (0 <= ai_exposure_index <= 1):
            return JsonResponse({
                'error': 'AI Exposure Index must be between 0 and 1'
            }, status=400)
        
        if not (0.5 <= tech_growth_factor <= 1.5):
            return JsonResponse({
                'error': 'Tech Growth Factor must be between 0.5 and 1.5'
            }, status=400)
        
        if years_experience < 0:
            return JsonResponse({
                'error': 'Years Experience must be positive'
            }, status=400)
        
        prediction = logistic_regression(
            ai_exposure_index,
            tech_growth_factor,
            years_experience
        )
        
        return JsonResponse({
            'prediction': prediction,
            'model': 'Logistic Regression',
            'input': {
                'ai_exposure_index': ai_exposure_index,
                'tech_growth_factor': tech_growth_factor,
                'years_experience': years_experience
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def predict_knn(request):
    """
    KNN Classification Prediction
    Predict Education Level using:
    - Average Salary
    - Years Experience
    - AI Exposure Index
    
    Endpoint: /predict_knn
    """
    try:
        data = json.loads(request.body)
        average_salary = float(data.get('average_salary', 50000))
        years_experience = float(data.get('years_experience', 0))
        ai_exposure_index = float(data.get('ai_exposure_index', 0))
        
        # Validate inputs
        if average_salary < 0:
            return JsonResponse({
                'error': 'Average Salary must be positive'
            }, status=400)
        
        if years_experience < 0:
            return JsonResponse({
                'error': 'Years Experience must be positive'
            }, status=400)
        
        if not (0 <= ai_exposure_index <= 1):
            return JsonResponse({
                'error': 'AI Exposure Index must be between 0 and 1'
            }, status=400)
        
        prediction = knn_classification(
            average_salary,
            years_experience,
            ai_exposure_index
        )
        
        return JsonResponse({
            'prediction': prediction,
            'model': 'K-Nearest Neighbors',
            'input': {
                'average_salary': average_salary,
                'years_experience': years_experience,
                'ai_exposure_index': ai_exposure_index
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def predict_polynomial(request):
    """
    Polynomial Regression Prediction (degree=3)
    Predict Automation Probability using AI Exposure Index
    
    Endpoint: /predict_polynomial
    Input: {"ai_exposure_index": float (0-1)}
    Output: {"prediction": float, "model": "Polynomial Regression"}
    """
    try:
        data = json.loads(request.body)
        ai_exposure_index = float(data.get('ai_exposure_index', 0))
        
        # Validate inputs
        if not (0 <= ai_exposure_index <= 1):
            return JsonResponse({
                'error': 'AI Exposure Index must be between 0 and 1'
            }, status=400)
        
        prediction = polynomial_regression(ai_exposure_index)
        
        return JsonResponse({
            'prediction': prediction,
            'model': 'Polynomial Regression (degree=3)',
            'input': {
                'ai_exposure_index': ai_exposure_index
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)

