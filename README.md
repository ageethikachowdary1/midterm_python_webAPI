# Enhanced Calculator – Midterm Project

## Overview

This project implements an advanced command-line calculator application using Python.  
It demonstrates object-oriented programming, multiple design patterns (Factory, Memento, Observer), automated testing, logging, CSV persistence, configuration management using environment variables, and CI/CD integration with GitHub Actions.

The project follows clean architecture principles and professional development practices.

---

## Implemented Features

### Arithmetic Operations

The calculator supports the following operations:

- add
- subtract
- multiply
- divide
- power
- root
- modulus
- int_divide
- percent
- abs_diff

All operations:
- Accept exactly two numeric inputs
- Validate input values
- Handle invalid cases (e.g., division by zero)
- Return correctly formatted results

---

## Design Patterns Used

### Factory Pattern
Used to dynamically create operation instances through `OperationFactory`.

### Memento Pattern
Used to implement:
- Undo
- Redo

The calculator maintains proper state history using snapshot restoration.

### Observer Pattern
Observers automatically respond after each calculation:

- LoggingObserver  
  Logs operation details to a file.

- AutoSaveObserver  
  Automatically saves calculation history to a CSV file using pandas.

---

## Command-Line Interface (REPL)

The application runs using a Read-Eval-Print Loop (REPL).

Supported Commands:

add  
subtract  
multiply  
divide  
power  
root  
modulus  
int_divide  
percent  
abs_diff  
history  
clear  
undo  
redo  
save  
load  
help  
exit  

Example:

```
calc> add 4 5
Result: 9.0
```

---

## History Management

- Stores calculations in memory
- Enforces maximum history size
- Supports undo and redo
- Saves history to CSV using pandas
- Loads history from CSV
- Handles missing or malformed files safely

---

## Logging

- Uses Python’s logging module
- Logs calculations and errors
- Writes logs to configured file location
- Uses appropriate logging levels (INFO, ERROR)

---

## Configuration Management

Configuration is managed using:

- `.env` file
- `python-dotenv`
- Default fallback values

Supported environment variables:

- CALCULATOR_LOG_DIR
- CALCULATOR_HISTORY_DIR
- CALCULATOR_MAX_HISTORY_SIZE
- CALCULATOR_AUTO_SAVE
- CALCULATOR_PRECISION
- CALCULATOR_MAX_INPUT_VALUE
- CALCULATOR_DEFAULT_ENCODING

If environment variables are not set, safe defaults are applied.

---

## Error Handling

Custom exceptions implemented:

- OperationError
- ValidationError
- PersistenceError

The application:
- Validates numeric input
- Prevents division by zero
- Handles invalid commands
- Handles file persistence errors
- Does not crash on invalid input

---

## Unit Testing

- 42 unit tests implemented
- Edge case testing included
- Undo/Redo tested
- CSV persistence tested
- Input validation tested
- REPL tested

### Test Coverage

97% test coverage achieved.

Run tests:

```
pytest
```

Run with coverage:

```
pytest --cov=app
```

CI enforces minimum 90% coverage.

---

## Continuous Integration (CI)

GitHub Actions workflow automatically:

- Checks out code
- Sets up Python
- Installs dependencies
- Runs tests
- Enforces 90% coverage threshold

Workflow file:

.github/workflows/python-app.yml

CI fails if coverage drops below 90%.

---

## Installation

### Clone Repository

```
git clone <repository_url>
cd project_directory
```

### Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

```
python main.py
```

---

## Project Structure

project_root/
├── app/
├── tests/
├── .github/workflows/
├── main.py
├── requirements.txt
├── README.md

---

## Technologies Used

- Python 3.12
- pytest
- pytest-cov
- pandas
- python-dotenv
- colorama
- Git
- GitHub Actions

---

## Learning Outcomes Demonstrated

- Git version control with structured commit history
- Linux command-line usage
- Automated testing
- CI/CD setup with GitHub Actions
- Object-oriented design
- Design pattern implementation
- CSV serialization with pandas
- Professional logging and error handling

---

## Final Status

- All mandatory features implemented
- Optional feature implemented (Color-coded output using colorama)
- 42 tests passing
- 97% coverage
- CI passing
- Clean commit history
- Professional project structure
