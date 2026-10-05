"""A command-line BMI calculator using kilograms and centimeters."""

# App input limits in centimeters; both endpoints are allowed.
MIN_HEIGHT_CM = 50
MAX_HEIGHT_CM = 250


def get_number(prompt):
    """Ask for a number, retrying when input cannot be converted.

    Args:
        prompt (str): The question shown to the user, including its unit.

    Returns:
        float: The entered number. The caller checks its allowed range.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            pass
        print("Please enter a number, such as 70 or 70.5.")


def get_weight():
    """Ask for weight within the allowed range.

    Returns:
        float: Weight greater than 0 and less than 1000 kilograms.
    """
    while True:
        weight_kg = get_number("\nWeight in kilograms (0 < weight < 1000): ")
        if 0 < weight_kg < 1000:
            return weight_kg
        print("Weight must be greater than 0 and less than 1000 kg.")


def get_height():
    """Ask for height until it falls within the app's allowed range.

    Returns:
        float: Height from MIN_HEIGHT_CM to MAX_HEIGHT_CM, inclusive.
    """
    while True:
        height_cm = get_number(
            f"Height in centimeters ({MIN_HEIGHT_CM}-{MAX_HEIGHT_CM}): "
        )
        if MIN_HEIGHT_CM <= height_cm <= MAX_HEIGHT_CM:
            return height_cm
        print(f"Height must be between {MIN_HEIGHT_CM} and {MAX_HEIGHT_CM} cm.")


def calculate_bmi(weight_kg, height_cm):
    """Calculate BMI from weight in kilograms and height in centimeters.

    Args:
        weight_kg (float): Weight greater than 0 and less than 1000 kg.
        height_cm (float): Height in centimeters within the app's limits.

    Returns:
        float: The unrounded BMI.

    Raises:
        ValueError: If weight or height is outside the allowed range.
    """
    # Check here too, because this function can be called without the prompts.
    if not 0 < weight_kg < 1000:
        raise ValueError("Weight must be greater than 0 and less than 1000 kg.")
    if not MIN_HEIGHT_CM <= height_cm <= MAX_HEIGHT_CM:
        raise ValueError(
            f"Height must be between {MIN_HEIGHT_CM} and {MAX_HEIGHT_CM} cm."
        )

    # The formula uses meters, so convert centimeters before squaring.
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi):
    """Find the standard adult category using the unrounded BMI.

    These categories apply to adults aged 20 and older.

    Args:
        bmi (float): A positive, finite BMI from calculate_bmi().

    Returns:
        str: Underweight, Healthy weight, Overweight, or Obesity.
    """
    # Each return ends the function, so later checks need only an upper limit.
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Healthy weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity"


def main():
    """Collect measurements, display BMI, and optionally calculate again.

    Returns:
        None.
    """
    print("Welcome to BMI Calculator!")
    print("Adult categories are for ages 20 and older.")
    print("BMI is a screening measure, not a medical diagnosis.")

    while True:
        weight_kg = get_weight()
        height_cm = get_height()
        bmi = calculate_bmi(weight_kg, height_cm)

        # Round only the displayed number, keeping category checks accurate.
        print(f"\nYour BMI: {bmi:.2f}")
        print(f"Adult category: {get_bmi_category(bmi)}")
        print("The category uses the BMI before rounding.")

        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            break

    print("Thanks for using BMI Calculator!")


if __name__ == "__main__":
    main()
