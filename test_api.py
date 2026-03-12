"""
Test script to verify Django API endpoints
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_slr():
    """Test Simple Linear Regression endpoint"""
    print("\n=== Testing Simple Linear Regression ===")
    response = requests.post(
        f"{BASE_URL}/predict_slr",
        json={"ai_exposure_index": 0.75}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

def test_mlr():
    """Test Multiple Linear Regression endpoint"""
    print("\n=== Testing Multiple Linear Regression ===")
    response = requests.post(
        f"{BASE_URL}/predict_mlr",
        json={
            "ai_exposure_index": 0.75,
            "tech_growth_factor": 1.2,
            "years_experience": 5,
            "average_salary": 75000
        }
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

def test_logistic():
    """Test Logistic Regression endpoint"""
    print("\n=== Testing Logistic Regression ===")
    response = requests.post(
        f"{BASE_URL}/predict_logistic",
        json={
            "ai_exposure_index": 0.75,
            "tech_growth_factor": 1.2,
            "years_experience": 5
        }
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

def test_knn():
    """Test KNN Classification endpoint"""
    print("\n=== Testing KNN Classification ===")
    response = requests.post(
        f"{BASE_URL}/predict_knn",
        json={
            "ai_exposure_index": 0.75,
            "tech_growth_factor": 1.2,
            "years_experience": 5
        }
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    print("Testing Django API Endpoints...")
    test_slr()
    test_mlr()
    test_logistic()
    test_knn()
    print("\n=== All Tests Completed ===")

