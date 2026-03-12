"""
ML Utilities - Mock ML Predictions
This file simulates trained ML model predictions.
In production, you would load actual .pkl model files.
"""

import numpy as np

# Exchange rate: 1 USD = 83 INR (approximate)
USD_TO_INR = 83


def simple_linear_regression(years_experience):
    """
    Simple Linear Regression: Predict Average Salary using Years Experience
    Formula: y = mx + c
    
    Returns: dict with 'annual' and 'monthly' salary predictions
    """
    # Simulated trained model coefficients (in INR)
    slope = 3500 * USD_TO_INR  # ₹290,500 increase per year
    intercept = 45000 * USD_TO_INR  # Base salary ₹37,35,000
    
    # Add some realistic variation
    noise = np.random.normal(0, 3000 * USD_TO_INR)
    
    prediction = slope * years_experience + intercept + noise
    
    # Clamp to reasonable salary range (in INR)
    prediction = max(30000 * USD_TO_INR, min(300000 * USD_TO_INR, prediction))
    
    # Return both annual and monthly salary
    annual_salary = round(prediction, 2)
    monthly_salary = round(prediction / 12, 2)
    
    return {
        'annual': annual_salary,
        'monthly': monthly_salary
    }


def multiple_linear_regression(ai_exposure_index, tech_growth_factor, years_experience, average_salary):
    """
    Multiple Linear Regression: Predict Automation Probability 2030
    Using: AI Exposure Index, Tech Growth Factor, Years Experience, Average Salary
    """
    # Simulated trained model coefficients
    coef_ai = 0.40
    coef_tech = 0.25
    coef_exp = 0.15
    coef_salary = 0.20
    intercept = 0.10
    
    # Add some realistic variation
    noise = np.random.normal(0, 0.02)
    
    # Normalize salary to reasonable scale (0-1)
    salary_normalized = min(average_salary / 200000, 1.0)
    
    prediction = (coef_ai * ai_exposure_index + 
                  coef_tech * tech_growth_factor + 
                  coef_exp * (years_experience / 20) +
                  coef_salary * salary_normalized +
                  intercept + noise)
    
    # Clamp to valid probability range (0-1)
    prediction = max(0, min(1, prediction))
    
    return round(prediction, 2)


def logistic_regression(ai_exposure_index, tech_growth_factor, years_experience):
    """
    Logistic Regression: Predict Risk Category (Low / Medium / High)
    Using: AI Exposure Index, Tech Growth Factor, Years Experience
    """
    # Calculate risk score
    risk_score = (0.45 * ai_exposure_index + 
                  0.30 * (1 - tech_growth_factor) + 
                  0.25 * (1 - min(years_experience / 15, 1)))
    
    # Add some variation
    noise = np.random.normal(0, 0.05)
    risk_score = risk_score + noise
    
    # Classify into categories
    if risk_score < 0.35:
        return "Low"
    elif risk_score < 0.65:
        return "Medium"
    else:
        return "High"


def knn_classification(average_salary, years_experience, ai_exposure_index):
    """
    KNN Classification: Predict Education Level
    Using: Average Salary, Years Experience, AI Exposure Index
    
    Possible outputs: High School, Bachelor's, Master's, PhD
    """
    # Create feature vector for education prediction
    # Higher salary + more experience + higher AI exposure = higher education
    education_score = (0.35 * min(average_salary / 150000, 1.0) + 
                       0.35 * min(years_experience / 20, 1.0) +
                       0.30 * ai_exposure_index)
    
    # Add some variation
    noise = np.random.normal(0, 0.05)
    education_score = education_score + noise
    
    # Classify into education levels
    if education_score < 0.25:
        return "High School"
    elif education_score < 0.50:
        return "Bachelor's"
    elif education_score < 0.75:
        return "Master's"
    else:
        return "PhD"


def polynomial_regression(ai_exposure_index):
    """
    Polynomial Regression: Predict Automation Probability using AI Exposure Index
    Uses degree=3 polynomial features
    
    Model: y = a*x^3 + b*x^2 + c*x + d
    """
    # Simulated trained polynomial model coefficients (degree=3)
    coef_cubic = 0.15
    coef_quadratic = -0.20
    coef_linear = 0.45
    coef_experience = 0.08
    intercept = 0.65
    
    # Add some realistic variation
    noise = np.random.normal(0, 0.02)
    
    # Calculate polynomial
    x = ai_exposure_index
    exp_normalized = 5 / 20  # Using default experience of 5
    
    prediction = (coef_cubic * x**3 + 
                  coef_quadratic * x**2 + 
                  coef_linear * x + 
                  coef_experience * exp_normalized +
                  intercept + noise)
    
    # Clamp to valid probability range (0-1)
    prediction = max(0, min(1, prediction))
    
    return round(prediction, 2)

