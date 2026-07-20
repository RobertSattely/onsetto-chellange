# Onsetto Engineering Challenge

This repository contains my solution to the Onsetto Engineering Challenge. The project is divided into two independent parts:

* **Part 1:** Browser Automation using Playwright
* **Part 2:** Python REST API Client

Each part is self-contained with its own virtual environment, dependencies, and configuration.

---

# Repository Structure

```text
Onsetto_Engineering_Challenge/
│
├── Part_One_Web_Scraping-Automation/
│   ├── .venv/
│   ├── .env
│   ├── requirements.txt
│   ├── run.py
│   └── ...
│
├── Part_Two_Python_API_Client/
│   ├── .venv/
│   ├── .env
│   ├── requirements.txt
│   ├── main.py
│   └── ...
│
└── README.md
```

---

# Technologies

* Python 3.14
* Playwright
* Requests
* python-dotenv

---

# Part 1 – Browser Automation

## Overview

This application automates the user workflow using Playwright.

The automation performs the following steps:

* Launches a browser session
* Authenticates with the provided credentials
* Completes the simulated MFA flow
* Navigates to the Account page
* Updates banking information
* Updates payment information
* Verifies that the updated values are displayed correctly
* Captures screenshots throughout the workflow for troubleshooting and validation

### Project Organization

* Page Object Model (POM)
* Utility helpers for logging and test data generation
* Validators for generated values
* Reusable helper classes

---

# Part 2 – Python API Client

## Overview

The API client performs the same business workflow using the published REST API.

Workflow:

1. Authenticate using email and password
2. Complete MFA verification
3. Store the bearer token
4. Update banking information
5. Update payment information
6. Display the masked confirmation values returned by the API

---

# API Features

* Reusable `ApiClient` class
* Session-based authentication
* Automatic Bearer token management
* Environment variable configuration
* Random test data generation
* Credit card validation using the Luhn algorithm
* Centralized logging
* Graceful error handling

---

# Configuration

Configuration is managed through a `.env` file.

Example:

```text
BASE_URL=https://zvyhufnwclhcvmgtqxwp.supabase.co/functions/v1/api-v1
EMAIL=your_email@example.com
PASSWORD=your_password
```

---

# Installation

Clone the repository.

## Part 1

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run:

```bash
python run.py
```

---

## Part 2

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# Assumptions

* The MFA verification code is always **1234**, as specified in the challenge.
* Authentication uses the two-step token exchange documented by the API.
* The API returns masked confirmation values after successful updates.

---

# Limitations

The provided API does not expose endpoints to retrieve banking or payment information after it has been updated.

Because of this, successful updates are validated by:

* Successful HTTP responses
* The masked confirmation values returned by the API

Without corresponding GET endpoints, independent verification of persisted data is not possible.

---

# Future Improvements

If this were expanded into a production application, the following enhancements would be valuable:

* Unit and integration testing with `pytest`
* Type-safe request and response models (Pydantic)
* Automatic retry logic with exponential backoff
* Structured JSON logging
* Static analysis with Ruff and MyPy
* Continuous Integration using GitHub Actions
* Docker containerization
* Enhanced observability and metrics

---

# Design Goals

The project emphasizes:

* Clean separation of responsibilities
* Reusable components
* Readable and maintainable code
* Secure configuration using environment variables
* Simple extension for future API endpoints

The implementation focuses on demonstrating practical Python engineering principles while remaining concise and easy to understand.