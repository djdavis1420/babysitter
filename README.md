# Babysitter Payment Calculator Kata

This application simulates a babysitter working and getting paid for one night.

## Prerequisites

```
IntelliJ IDEA with Python Plugin (or PyCharm)
```

## Installing

- Clone the repository at "https://github.com/djdavis1420/babysitter"
- In your terminal/console, navigate to the project's root directory
- If necessary ... 
    - "pip install virtualenv" to install virtualenv to your global environment
    - "virtualenv venv" to create a virtualenv for this project 
- Activate your virtual environment
    - "source ./venv/Scripts/activate" for Windows
    - "source ./venv/bin/activate" for Mac
- Type "pip install -Ur test_reqs.txt" to install dependencies
    - Pytest and Mock will be installed in the virtual environment
- Deactivate the virtual environment (eg, "deactivate")

## Running the Console Application

 - Right-click on console_app.py and select "Run 'console_app'".
 - With the assumptions below in mind, follow the prompts in the console.
 
## Assumptions
- Rates of Pay will always be valid dollar values (without a dollar sign)
    - Rates of Pay can be entered as integers (15)
    - Rates of Pay can be entered as float (12.50)
- Times will always be in 24-hour format __*on the hour*__.
    - Jobs will always start in the PM (between 1200 and 2400, inclusive).
    - Jobs will always end in the AM (between 000 and 1100, inclusive)

## Built With

- [IntelliJ IDEA](https://www.jetbrains.com/idea/) - Integrated Development Environment
- [PyTest](https://docs.pytest.org/en/latest/) - Testing Framework for Python
- [mock](https://docs.python.org/dev/library/unittest.mock.html) - Testing Library for Python