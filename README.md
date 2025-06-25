# SauceDemo_Project

This is a Python-based Selenium automation project built for testing the full end-to-end user flow on [SauceDemo](https://www.saucedemo.com/), a demo site used to simulate e-commerce flows.

---

##  Project Structure

SauceDemo Project/
│
├── Pages/
│ ├── framework.py # Reusable helper methods (URL check, waits, etc.)
│ ├── homepage.py # Interactions and verifications on login/home page
│ ├── addtoCart.py # Product selection and cart operations
│ ├── checkout.py # Cart review and checkout initiation
│ └── checkOutSteps.py # Entering checkout info, confirming and completing order
│
├── Tests/
│ └── test_db.py # Main pytest file running the full user flow

---

## 🛠️ Setup Instructions

1. **Install Python (Recommended: Python 3.11+)**
   - Download from: https://www.python.org/downloads/

**requirements**
selenium
pytest
pytest-html

** Test Coverage**

 Login and element verification

 Product selection and cart functionality

 Checkout flow 

 User detail submission and validation

 Final order confirmation

 Return to home (back button)

 URL and text assertions


** Challenges Faced**
 
1) Element timing issues required explicit waits and scrolls using JavaScript.

2) The test originally failed by navigating too quickly before the "Checkout Complete" page fully loaded.

3) Some selectors were fragile and needed refactoring for better reliability.

**Improvements for Production**

Use of logging instead of print()

Integration with reporting tools (Allure, Jenkins, etc.)

Data-driven testing using fixtures or external files

Parallel execution using pytest-xdist

Retry logic for flaky interactions
