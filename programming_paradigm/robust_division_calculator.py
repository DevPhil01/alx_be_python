# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely performs division of two values provided as strings.
    Handles non-numeric inputs and division by zero gracefully.

    Args:
        numerator (str): The numerator as a string (from command line)
        denominator (str): The denominator as a string (from command line)

    Returns:
        str: A user-friendly message with the result or appropriate error
    """
    # First, try to convert both inputs to float
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Now attempt the division
    try:
        result = num / den
        return f"The result of the division is {result}"
        # You can also use: return f"The result of the division is {result:.1f}" for cleaner output
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
