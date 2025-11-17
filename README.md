# Demoblaze Test Automation

For detailed documentation, read documentation.md

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/aizazayubi/test-automation-project.git
cd cd test-automation-project
````

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# Linux / Mac
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

4. Run all test scenarios:

```bash
pytest tests/test_all_scenarios.py -v --html=report.html --self-contained-html
```

> Open `report.html` to see the results.

---

## Notes

* The CI/CD workflow (`ci.yml`) currently runs **login tests only**.
* To run all scenarios in CI/CD, update the workflow file and change the test file name to:

```yaml
pytest tests/test_all_scenarios.py
```

```


