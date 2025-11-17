# Demoblaze Test Automation Project

This project demonstrates a robust test automation framework for the **Demoblaze** e-commerce website using **Python**, **Playwright**, and **Pytest**.  
It includes **Page Object Model (POM)**, **HTML test reporting**, and **CI/CD workflow**.

---

## Application Under Test
[Demoblaze E-Commerce Website](https://www.demoblaze.com/)

---

## Project Structure

project-root/
│
├── tests/
│ ├── pages/
│ │ ├── login_page.py # Page Object for Login Page
│ │ ├── home_page.py # Page Object for Home Page
│ │ └── cart_page.py # Page Object for Cart Page
│ ├── test.py # Main test file containing all scenarios
│ └── conftest.py # Pytest fixtures for browser, page, screenshots
│
├── .github/workflows/ci.yml # GitHub Actions workflow for CI/CD
├── requirements.txt # Python dependencies
├── pytest.ini # Pytest configuration
├── report.html # HTML test report (generated)
└── README.md # This documentation
