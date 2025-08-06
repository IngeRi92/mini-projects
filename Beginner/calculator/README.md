# Simple Calculator

A command-line calculator application built in Python that performs basic mathematical operations with user-friendly interface and error handling.

## Features

- Basic Operations: Addition, Subtraction, Multiplication, Division
- Advanced Operations: Power calculation, Square root
- Error Handling:
  - Division by zero protection
  - Negative square root protection
  - Invalid input validation
- User-Friendly Interface: Clear menu system
- Continuous Operation: Perform multiple calculations in one session

## How to Run

1. Make sure you have Python 3.x installed
2. Clone or download the calculator.py file
3. Open terminal/command prompt
4. Navigate to the file location

## Run the program:

```bash
python calculator.py
```

## Usage Example

=================
SIMPLE CALCULATOR
=================
Select operation:

1. Addition (+)
2. Subtraction (-)
3. Multiplication (\*)
4. Division (/)
5. Power (^)
6. Square Root (√)
7. # Exit

Enter choice (1-7): 1
Enter first number: 15
Enter second number: 25

15.0 + 25.0 = 40.0

## Technical Details

Operations Supported:

- Addition (+): Adds two numbers
- Subtraction (-): Subtracts second number from first
- Multiplication (×): Multiplies two numbers
- Division (÷): Divides first number by second (with zero-division check)
- Power (^): Raises first number to the power of second
- Square Root (√): Calculates square root (with negative number check)

## Error Handling:

- Input validation for menu choices
- Number format validation
- Division by zero prevention
- Negative square root prevention
- General exception handling

## File Structure

```bash
/calculator
├── calculator.py # Main calculator program
├── README.md # This documentation
└── requirements.txt # Python dependencies (none needed)
```

## Requirements

- Python 3.x (uses built-in libraries only)
- No external dependencies required

## Future Improvements

Potential enhancements for this project:

- GUI version using tkinter
- Scientific calculator functions (sin, cos, tan, log)
- History of calculations
- Memory functions (M+, M-, MC, MR)
- Configuration file for customization

## Learning Objectives

This project demonstrates:

- Functions: Modular code organization
- Error Handling: Try-catch blocks and input validation
- User Input: Getting and validating user input
- Control Flow: Loops and conditional statements
- String Formatting: Professional output formatting
- Documentation: Code comments and README creation
