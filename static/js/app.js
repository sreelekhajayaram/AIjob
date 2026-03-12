/**
 * AI Jobs Risk Prediction - JavaScript
 * Handles Fetch API calls to Django backend
 */

// API Base URL - points to Django endpoints
const API_BASE = '';

/**
 * Show loading state in result section
 */
function showLoading(resultId) {
    const resultSection = document.getElementById(resultId);
    resultSection.className = 'result-section result-loading';
    resultSection.innerHTML = `
        <div class="spinner"></div>
        <span style="margin-left: 10px; color: var(--text-secondary); font-size: 0.9rem;">Processing...</span>
    `;
}

/**
 * Show error state in result section
 */
function showError(resultId, message) {
    const resultSection = document.getElementById(resultId);
    resultSection.className = 'result-section result-error';
    resultSection.innerHTML = `
        <div class="error-message">
            <i class="fas fa-exclamation-circle"></i>
            <span>${message}</span>
        </div>
    `;
}

/**
 * Show success state for salary predictions (Simple Linear Regression)
 */
function showSalaryResult(resultId, prediction, model) {
    const resultSection = document.getElementById(resultId);
    resultSection.className = 'result-section result-success';
    resultSection.innerHTML = `
        <div style="text-align: center; width: 100%;">
            <div class="result-label">Predicted Average Salary</div>
            <div class="result-value">
                Annual: ₹${prediction.annual.toLocaleString()}
            </div>
            <div class="result-value" style="margin-top: 8px;">
                Monthly: ₹${prediction.monthly.toLocaleString()}
            </div>
            <div class="result-model">${model}</div>
        </div>
    `;
}

/**
 * Show success state for probability predictions (MLR, Polynomial)
 */
function showProbabilityResult(resultId, prediction, model) {
    const resultSection = document.getElementById(resultId);
    resultSection.className = 'result-section result-success';
    resultSection.innerHTML = `
        <div style="text-align: center; width: 100%;">
            <div class="result-label">Automation Probability</div>
            <div class="result-value">
                ${prediction}
            </div>
            <div class="result-model">${model}</div>
        </div>
    `;
}

/**
 * Show success state for category predictions (Logistic - Risk Category)
 */
function showCategoryResult(resultId, prediction, model) {
    const resultSection = document.getElementById(resultId);
    
    // Determine risk class for styling
    let riskClass = '';
    if (prediction === 'High') {
        riskClass = 'high-risk';
    } else if (prediction === 'Medium') {
        riskClass = 'medium-risk';
    } else {
        riskClass = 'low-risk';
    }
    
    resultSection.className = 'result-section result-success';
    resultSection.innerHTML = `
        <div style="text-align: center; width: 100%;">
            <div class="result-label">Risk Category</div>
            <div class="result-value ${riskClass}">${prediction}</div>
            <div class="result-model">${model}</div>
        </div>
    `;
}

/**
 * Show success state for Education Level predictions (KNN)
 */
function showEducationResult(resultId, prediction, model) {
    const resultSection = document.getElementById(resultId);
    
    // Determine education class for styling
    let eduClass = '';
    if (prediction === "PhD") {
        eduClass = 'high-risk';
    } else if (prediction === "Master's") {
        eduClass = 'medium-risk';
    } else if (prediction === "Bachelor's") {
        eduClass = 'low-risk';
    } else {
        eduClass = '';
    }
    
    resultSection.className = 'result-section result-success';
    resultSection.innerHTML = `
        <div style="text-align: center; width: 100%;">
            <div class="result-label">Education Level</div>
            <div class="result-value ${eduClass}">${prediction}</div>
            <div class="result-model">${model}</div>
        </div>
    `;
}

/**
 * Simple Linear Regression Prediction
 * Predicts Average Salary using Years Experience
 */
async function predictSLR() {
    const resultId = 'slr-result';
    const experience = parseFloat(document.getElementById('slr-experience').value);
    
    // Validate input
    if (isNaN(experience) || experience < 0) {
        showError(resultId, 'Please enter valid Years of Experience');
        return;
    }
    
    showLoading(resultId);
    
    try {
        const response = await fetch('/predict_slr', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                years_experience: experience
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showSalaryResult(resultId, data.prediction, data.model);
        } else {
            showError(resultId, data.error || 'Prediction failed');
        }
    } catch (error) {
        showError(resultId, 'Network error. Please try again.');
        console.error('Error:', error);
    }
}

/**
 * Multiple Linear Regression Prediction
 * Predicts Automation Probability 2030 using multiple features
 */
async function predictMLR() {
    const resultId = 'mlr-result';
    
    const aiExposure = parseFloat(document.getElementById('mlr-ai-exposure').value);
    const techGrowth = parseFloat(document.getElementById('mlr-tech-growth').value);
    const experience = parseFloat(document.getElementById('mlr-experience').value);
    const salary = parseFloat(document.getElementById('mlr-salary').value);
    
    // Validate inputs
    if (isNaN(aiExposure) || aiExposure < 0 || aiExposure > 1) {
        showError(resultId, 'Please enter a valid AI Exposure Index (0-1)');
        return;
    }
    
    if (isNaN(techGrowth) || techGrowth < 0.5 || techGrowth > 1.5) {
        showError(resultId, 'Please enter a valid Tech Growth Factor (0.5-1.5)');
        return;
    }
    
    if (isNaN(experience) || experience < 0) {
        showError(resultId, 'Please enter valid Years of Experience');
        return;
    }
    
    if (isNaN(salary) || salary < 0) {
        showError(resultId, 'Please enter a valid Average Salary');
        return;
    }
    
    showLoading(resultId);
    
    try {
        const response = await fetch('/predict_mlr', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                ai_exposure_index: aiExposure,
                tech_growth_factor: techGrowth,
                years_experience: experience,
                average_salary: salary
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showProbabilityResult(resultId, data.prediction, data.model);
        } else {
            showError(resultId, data.error || 'Prediction failed');
        }
    } catch (error) {
        showError(resultId, 'Network error. Please try again.');
        console.error('Error:', error);
    }
}

/**
 * Polynomial Regression Prediction (degree=3)
 * Predicts Automation Probability using AI Exposure Index
 */
async function predictPolynomial() {
    const resultId = 'poly-result';
    const aiExposure = parseFloat(document.getElementById('poly-ai-exposure').value);
    
    // Validate input
    if (isNaN(aiExposure) || aiExposure < 0 || aiExposure > 1) {
        showError(resultId, 'Please enter a valid AI Exposure Index (0-1)');
        return;
    }
    
    showLoading(resultId);
    
    try {
        const response = await fetch('/predict_polynomial', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                ai_exposure_index: aiExposure
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showProbabilityResult(resultId, data.prediction, data.model);
        } else {
            showError(resultId, data.error || 'Prediction failed');
        }
    } catch (error) {
        showError(resultId, 'Network error. Please try again.');
        console.error('Error:', error);
    }
}

/**
 * Logistic Regression Prediction
 * Predicts Risk Category (Low/Medium/High)
 */
async function predictLogistic() {
    const resultId = 'logistic-result';
    
    const aiExposure = parseFloat(document.getElementById('logistic-ai-exposure').value);
    const techGrowth = parseFloat(document.getElementById('logistic-tech-growth').value);
    const experience = parseFloat(document.getElementById('logistic-experience').value);
    
    // Validate inputs
    if (isNaN(aiExposure) || aiExposure < 0 || aiExposure > 1) {
        showError(resultId, 'Please enter a valid AI Exposure Index (0-1)');
        return;
    }
    
    if (isNaN(techGrowth) || techGrowth < 0.5 || techGrowth > 1.5) {
        showError(resultId, 'Please enter a valid Tech Growth Factor (0.5-1.5)');
        return;
    }
    
    if (isNaN(experience) || experience < 0) {
        showError(resultId, 'Please enter valid Years of Experience');
        return;
    }
    
    showLoading(resultId);
    
    try {
        const response = await fetch('/predict_logistic', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                ai_exposure_index: aiExposure,
                tech_growth_factor: techGrowth,
                years_experience: experience
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showCategoryResult(resultId, data.prediction, data.model);
        } else {
            showError(resultId, data.error || 'Prediction failed');
        }
    } catch (error) {
        showError(resultId, 'Network error. Please try again.');
        console.error('Error:', error);
    }
}

/**
 * KNN Classification Prediction
 * Predicts Education Level (High School/Bachelor's/Master's/PhD)
 */
async function predictKNN() {
    const resultId = 'knn-result';
    
    const salary = parseFloat(document.getElementById('knn-salary').value);
    const experience = parseFloat(document.getElementById('knn-experience').value);
    const aiExposure = parseFloat(document.getElementById('knn-ai-exposure').value);
    
    // Validate inputs
    if (isNaN(salary) || salary < 0) {
        showError(resultId, 'Please enter a valid Average Salary');
        return;
    }
    
    if (isNaN(experience) || experience < 0) {
        showError(resultId, 'Please enter valid Years of Experience');
        return;
    }
    
    if (isNaN(aiExposure) || aiExposure < 0 || aiExposure > 1) {
        showError(resultId, 'Please enter a valid AI Exposure Index (0-1)');
        return;
    }
    
    showLoading(resultId);
    
    try {
        const response = await fetch('/predict_knn', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                average_salary: salary,
                years_experience: experience,
                ai_exposure_index: aiExposure
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showEducationResult(resultId, data.prediction, data.model);
        } else {
            showError(resultId, data.error || 'Prediction failed');
        }
    } catch (error) {
        showError(resultId, 'Network error. Please try again.');
        console.error('Error:', error);
    }
}

/**
 * Get CSRF Token for Django
 * Required for POST requests
 */
function getCSRFToken() {
    // Try to get CSRF token from cookie
    const name = 'csrftoken';
    let cookieValue = null;
    
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    
    // If no cookie, return empty string (will work with @csrf_exempt decorator)
    return cookieValue || '';
}

// Add keyboard support - Enter key triggers prediction
document.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        const activeElement = document.activeElement;
        if (activeElement.tagName === 'INPUT') {
            // Find parent card and trigger predict button
            const card = activeElement.closest('.prediction-card');
            if (card) {
                const button = card.querySelector('.predict-btn');
                if (button) {
                    button.click();
                }
            }
        }
    }
});

// Add input validation visual feedback
document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener('input', function() {
        const min = parseFloat(this.min);
        const max = parseFloat(this.max);
        const value = parseFloat(this.value);
        
        if (!isNaN(value) && (value < min || value > max)) {
            this.style.borderColor = '#e74c3c';
        } else {
            this.style.borderColor = '#e9ecef';
        }
    });
});

console.log('AI Jobs Automation & Career Prediction Dashboard - JavaScript Loaded');

