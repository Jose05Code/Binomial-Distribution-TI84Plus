# Binomial Distribution TI-84 Plus

A Python-based binomial distribution calculator that mimics the functionality of TI-84 Plus calculators. This tool provides an interactive command-line interface for calculating various binomial distribution probabilities.

## Overview

This project implements binomial distribution calculations commonly found in TI-84 Plus calculators. It allows users to calculate:

- P(x > a) - Probability that x is greater than a
- P(x >= a) - Probability that x is greater than or equal to a
- P(x < a) - Probability that x is less than a
- P(x <= a) - Probability that x is less than or equal to a
- P(x = a) - Probability that x equals a

The calculator uses the binomial probability mass function (PDF) and cumulative distribution function (CDF) to compute these probabilities based on user-provided parameters (number of trials, probability of success, and value of interest).

## Screenshot

<!-- Placeholder for screenshot -->
*Screenshot of the application will be added here*

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Jose05Code/Binomial-Distribution-TI84Plus.git
   cd Binomial-Distribution-TI84Plus
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the package in editable mode (optional, for development):
   ```bash
   pip install -e .
   ```

### Docker Installation (Alternative)

If you prefer using Docker:

1. Build and run using Docker Compose:
   ```bash
   docker-compose up --build
   ```

This will run the test suite automatically.

## Usage

### Running the Calculator

To start the interactive binomial distribution calculator:

```bash
python src/BINODIST.py
```

### Using the Calculator

1. When the program starts, you'll see a menu with 5 options
2. Enter your choice (1-5) based on which probability you want to calculate
3. Provide the following parameters when prompted:
   - **n** (number of trials): A non-negative integer representing the total number of trials
   - **p** (probability of success): A decimal number between 0 and 1 representing the probability of success on a single trial
   - **a** (value): A non-negative integer representing the value you're interested in

### Example

Let's calculate P(x = 3) for a binomial distribution with n=10 trials and p=0.5 probability:

```
===============================
Welcome to the Bino Library
1. P(x > a)
2. P(x >= a)
3. P(x < a)
4. P(x <= a)
5. P(x = a)
===============================

Enter your choice (1-5): 5

Calculating P(x = a)...

Enter the number of trials (n >= 0): 10

Enter the probability of success in decimal (0 <= p <= 1): 0.5

Enter the value of a (a >= 0): 3

The answer is:  0.1171875
Push enter to continue.
```

### Using the Library in Your Code

You can also use the mathematical functions directly in your Python code:

```python
from src import LIB_MATH as math

# Calculate binomial PDF: P(X = k)
probability = math.binopdf(n=10, p=0.5, a=3)
print(f"P(X = 3) = {probability}")

# Calculate binomial CDF: P(X <= k)
cumulative = math.binocdf(n=10, p=0.5, a=3)
print(f"P(X <= 3) = {cumulative}")

# Calculate combinations: nCr
combinations = math.nCr(n=10, a=3)
print(f"10C3 = {combinations}")
```

## Running Tests

The project includes unit tests for the mathematical functions. To run the tests:

```bash
pytest test/test_math.py -v
```

Or using Docker:

```bash
docker-compose up
```

## Transferring to TI-84 Plus

**Note:** This is a Python implementation and runs on computers, not directly on TI-84 Plus calculators. However, it provides the same binomial distribution calculations that are available on TI-84 Plus calculators.

If you want to use binomial distribution functions on an actual TI-84 Plus calculator:
- Use the built-in `binompdf()` and `binomcdf()` functions
- Access them via: `2nd` → `VARS` (DISTR) → `binompdf()` or `binomcdf()`

This Python tool can be used for:
- Learning and understanding binomial distributions
- Checking your TI-84 Plus calculator results
- Performing calculations when a physical calculator is not available
- Batch processing multiple calculations

## Project Structure

```
Binomial-Distribution-TI84Plus/
├── src/
│   ├── BINODIST.py      # Main program with interactive menu
│   ├── LIB_BIN.py       # User interface and probability calculation functions
│   ├── LIB_MATH.py      # Core mathematical functions (nCr, binopdf, binocdf)
│   └── __init__.py      # Package initialization
├── test/
│   └── test_math.py     # Unit tests for mathematical functions
├── requirements.txt     # Python dependencies
├── setup.py            # Package setup configuration
├── dockerfile          # Docker configuration
├── docker-compose.yaml # Docker Compose configuration
└── README.md          # This file
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

The MIT License allows you to:
- Use the software for any purpose
- Modify the software
- Distribute the software
- Use the software privately
- Sell copies of the software

## Contributing

Contributions are welcome! Here's how you can help:

### Reporting Issues

If you find a bug or have a suggestion:
1. Check if the issue already exists in the [Issues](https://github.com/Jose05Code/Binomial-Distribution-TI84Plus/issues) section
2. If not, create a new issue with a clear description and steps to reproduce (for bugs)

### Submitting Changes

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/YourFeature`)
3. Make your changes
4. Write or update tests as needed
5. Ensure all tests pass (`pytest test/`)
6. Commit your changes (`git commit -m 'Add some feature'`)
7. Push to your branch (`git push origin feature/YourFeature`)
8. Open a Pull Request with a clear description of your changes

### Coding Standards

- Follow PEP 8 style guidelines for Python code
- Write meaningful commit messages
- Add tests for new functionality
- Update documentation as needed

## Contact

- **Author:** Jose
- **Repository:** [Jose05Code/Binomial-Distribution-TI84Plus](https://github.com/Jose05Code/Binomial-Distribution-TI84Plus)

For questions or support, please open an issue on GitHub.

## Acknowledgments

- Inspired by the binomial distribution functions available on TI-84 Plus calculators
- Built for educational purposes to help students and professionals understand binomial distributions
