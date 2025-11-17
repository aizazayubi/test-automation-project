# Demoblaze Test Automation Project

This project demonstrates automated testing for the [Demoblaze](https://www.demoblaze.com/) e-commerce website using **Python**, **Playwright**, and **Pytest**.  
It follows **Page Object Model (POM)** principles and includes **HTML reporting** and **CI/CD readiness**.

---

## Project Structure

```

project-root/
│
├── tests/
│   ├── pages/
│   │   ├── login_page.py      # Login page actions
│   │   ├── home_page.py       # Home page actions (select products)
│   │   └── cart_page.py       # Cart page actions (add/remove items)
│   ├── test.py                # Main test file implementing all scenarios
│   └── conftest.py            # Fixtures: browser, page setup, screenshots
│
├── .github/workflows/ci.yml   # CI/CD workflow
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration
├── report.html                # Generated HTML report
└── README.md                  # Project documentation

````

---

## Test Scenarios

1. **Valid Login**  
   - Login with valid credentials.  
   - Assert that the `"Welcome, username"` message is visible.  

2. **Invalid Login**  
   - Login with incorrect credentials.  
   - Assert the login modal remains visible or error is shown.  

3. **Add Item to Cart**  
   - Select a product on the Home Page.  
   - Add it to the cart.  
   - Verify the product appears in the Cart Page.  

4. **Add Non-existent Product / Invalid Product**  
   - Attempt to select a product that does not exist.  
   - Assert an exception is raised or product is not found.  

5. **Login → Add Product → Logout**  
   - Complete user flow: login, add product to cart, then logout.  
   - Assert the login button is visible after logout.

---

## Suggestions for Maintainability & Improvements

- **Page Object Model (POM):** Centralize locators and actions for each page.  
- **Fixtures:** Reusable browser and page setup reduces duplicate code.  
- **Screenshots on Failure:** Capture screenshots automatically to help debugging.  
- **CI/CD:** Configure GitHub Actions to run tests on push/pull request and upload HTML reports.  
- **Scalability:** Add separate configuration files for credentials, URLs, and test data.  
- **Future Enhancements:**  
  - Include additional pages (checkout, product details, categories).  
  - Parametrize product selection for broader coverage.  
  - Cross-browser testing (Chromium, Firefox, WebKit).  

---

## Test Execution

- Run all tests:

```bash
pytest tests/test.py -v --html=report.html --self-contained-html
````

* Open `report.html` to view detailed results.

```

---

This version is **compact, explanatory, and submission-ready**. It focuses on **five scenarios, project structure, and practical suggestions** without overwhelming details.  

If you want, I can also create a **slightly more visual version** with **tables for scenarios and assertions**, which often looks better in GitHub. Do you want me to do that?
```
