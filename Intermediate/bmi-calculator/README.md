# BMI Calculator

A simple command-line app that calculates body mass index (BMI) from
weight in kilograms and height in centimeters.

## Features

- Accept whole numbers or decimals, such as `70` or `70.5`
- Retry blank, nonnumeric, or out-of-range input
- Accept weights greater than 0 and less than 1000 kg
- Accept heights from 50 to 250 cm, including both endpoints
- Display BMI to two decimal places and its adult category
- Calculate again without restarting the program
- Use only Python's standard library

## How to Run

1. Make sure you have Python 3 installed. No extra packages are needed.
2. From the project root, run:

   ```bash
   python Intermediate/bmi-calculator/bmi_calculator.py
   ```

   Or, from this folder, run `python bmi_calculator.py`.

3. Enter your weight in kilograms and height in centimeters. Use a dot
   for decimal numbers and enter only the number, without a unit suffix.
   Weight must be greater than 0 and less than 1000 kg.
   Height must be between 50 and 250 cm. An out-of-range height asks you
   to enter height again without re-entering weight.
4. Enter `y` or `yes` to calculate again (case-insensitive). Any other
   response ends the program.

## Example

```text
Welcome to BMI Calculator!
Adult categories are for ages 20 and older.
BMI is a screening measure, not a medical diagnosis.

Weight in kilograms (0 < weight < 1000): 70
Height in centimeters (50-250): 175

Your BMI: 22.86
Adult category: Healthy weight
The category uses the BMI before rounding.

Calculate again? (y/n): n
Thanks for using BMI Calculator!
```

## How the Code Works

1. `get_number()` uses `float()` to convert input into a number.
   A `while` loop repeats the question if `try`/`except` catches a
   conversion error. `get_weight()` checks `0 < weight_kg < 1000`.
   `get_height()` checks the inclusive height limits defined by
   `MIN_HEIGHT_CM` and `MAX_HEIGHT_CM`. These are app input limits, not
   medical thresholds; change the constants to adjust the allowed range.
2. `calculate_bmi()` also validates weight and height so function calls respect
   the same limits, then converts centimeters to meters and applies the formula:

   ```text
   BMI = weight in kilograms / (height in meters ** 2)
   Example: 70 / (1.75 ** 2) = approximately 22.86
   ```

   In Python, `** 2` means "squared."
3. `get_bmi_category()` uses `if` statements to find the adult category.
4. `main()` connects the functions and handles repeat calculations.
   The format `:.2f` displays two decimal places without changing the
   value used to select the category.

The `if __name__ == "__main__":` block starts the app when run directly,
while allowing its functions to be imported without starting the prompts.

## Adult BMI Categories

| BMI before rounding | Category |
| --- | --- |
| Below 18.5 | Underweight |
| 18.5 to less than 25 | Healthy weight |
| 25 to less than 30 | Overweight |
| 30 or greater | Obesity |

These categories are for adults aged 20 and older. Children and teens
need an age-specific assessment. BMI is a screening measure, not a
diagnosis, and does not distinguish muscle from fat.

Near a category boundary, the rounded display may look like the next
category: a BMI of `24.999` displays as `25.00` but remains below 25.

## Ideas to Try Next

- Support pounds and inches as an alternative input option
- Add a Tkinter interface
- Save calculation results to a CSV file

---

Project for learning purposes.
