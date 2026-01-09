# 📌 LLM-Assisted BDD Functional Testing Prototype

This project demonstrates an end-to-end automated pipeline that converts plain English requirements into executable BDD (Behavior-Driven Development) tests using an LLM and runs them with Behave. The system uses Groq LLM (`llama-3.1-8b-instant`) to generate test scenarios, Python + Behave to execute BDD tests, and automated validation and feature file generation to reduce manual effort.

---

## 🚀 How the Pipeline Works

Requirement (English)  
↓  
LLM generates BDD scenarios (Gherkin format)  
↓  
validate.py filters output and selects the happy path  
↓  
Feature file auto-written to `/features/login.feature`  
↓  
Behave executes Python step definitions  
↓  
PASS / FAIL report generated

No `.feature` file is manually edited in this workflow—everything is derived dynamically.


---

### 1 Install dependencies
```bash
pip install behave groq python-dotenv

### 2 Create a .env file
GROQ_API_KEY=your-key-here

### 3 (Optional) Activate your virtual env
conda activate jupyter-env

---

## How to Run the System
# Step 1 — Generate BDD scenarios
python3 validate.py
#Step 2 — Execute tests
behave

## Default Requirement
A registered user should be able to log in with valid credentials and view their dashboard.
## Example generated scenario:
Scenario: Successful login
  Given I am on the log in page
  When I enter valid credentials and submit the form
  Then I should see my dashboard

🙌 Author

Meghana Kommana
LLM-Assisted Functional Testing Prototype — Case Study Submission
Jan 2026 Internship Evaluation