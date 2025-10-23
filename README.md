# Binomial Distribution TI-84 Plus

<img width="244" height="184" alt="Capture5-1760557063143" src="https://github.com/user-attachments/assets/c3b63487-9b66-434a-a2df-f48de3aa149f" />

A Python-based binomial distribution calculator that mimics the functionality of TI-84 Plus calculators. This tool provides an interactive command-line interface for calculating various binomial distribution probabilities.

## Overview

This project implements binomial distribution calculations commonly found in TI-84 Plus calculators. It allows users to calculate:

- P(x > a) - Probability that x is greater than a
- P(x >= a) - Probability that x is greater than or equal to a
- P(x < a) - Probability that x is less than a
- P(x <= a) - Probability that x is less than or equal to a
- P(x = a) - Probability that x equals a

The calculator uses the binomial probability mass function (PDF) and cumulative distribution function (CDF) to compute these probabilities based on user-provided parameters (number of trials, probability of success, and value of interest).

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

## How Install

This project is intended to run on a TI‑84 Plus CE (Python edition). To transfer a program to your calculator, use TI Connect™ CE (Windows or macOS) and follow the steps below.

Prepare the program file

- Download the release for the calculator from the project's Releases page (the release for the calculator contains only the files intended for the TI‑84 Plus CE).
- If you downloaded a release archive, extract it. If the release contains multiple files, the file you should open in the calculator is `BINODIST.py`.

Transfer with TI Connect CE (Windows / macOS)

1. Install TI Connect CE from Texas Instruments: https://education.ti.com/en/products/computer-software/ti-connect-ce-sw
2. Connect your TI‑84 Plus CE to your computer with the USB cable.
3. Open TI Connect CE and open Device Explorer.
4. In Device Explorer, open the calculator's Python folder.
5. Drag-and-drop your `.py` file into the Python folder (or use "Send to Device").
6. On the calculator open the Python app, find the program and run it.

Notes for Linux users

- TI Connect CE doesn't have a native Linux version. Options:
	- Run TI Connect CE under WINE or in a Windows VM and use Device Explorer there.
	- Transfer the file from a Windows or macOS machine that has TI Connect CE installed.

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


### Project Structure

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


### Coding Standards

- Follow PEP 8 style guidelines for Python code
- Write meaningful commit messages
- Add tests for new functionality
- Update documentation as needed


### For questions or support, please open an issue on GitHub.
