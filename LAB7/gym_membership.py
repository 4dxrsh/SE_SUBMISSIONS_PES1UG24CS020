import math


def parse_plan(code):
    """'GOLD-12' -> ('GOLD', 12). Returns None for invalid input."""
    if not isinstance(code, str):
        return None
    parts = code.split('-')
    if len(parts) != 2:
        return None
    plan, months = parts[0].strip(), parts[1].strip()
    if not plan.isalpha() or not months.isdecimal():
        return None
    try:
        months = int(months)
    except ValueError:
        return None
    if months <= 0:
        return None
    return plan.upper(), months


def calculate_bmi(data):
    """'70,1.75' -> 22.9. Returns None for invalid input."""
    if not isinstance(data, str):
        return None
    parts = data.split(',')
    if len(parts) != 2:
        return None
    try:
        weight = float(parts[0])
        height = float(parts[1])
        if not (math.isfinite(weight) and math.isfinite(height)):
            return None
        if weight <= 0 or height <= 0:
            return None
        bmi = weight / (height ** 2)
        if not math.isfinite(bmi):
            return None
        return round(bmi, 1)
    except (ValueError, TypeError, ZeroDivisionError, OverflowError):
        return None


def average_workout(minutes):
    """'45 60 30' -> 45. Returns None for invalid input."""
    if not isinstance(minutes, str):
        return None
    tokens = minutes.split()
    if not tokens:
        return None
    try:
        values = [int(t) for t in tokens]
    except ValueError:
        return None
    if any(v < 0 for v in values):
        return None
    return sum(values) // len(values)


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    if result is None:
        print("Invalid plan code. Expected format: NAME-MONTHS (e.g. GOLD-12)")
    else:
        print("Plan and Months:", result)

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    if result is None:
        print("Invalid input. Expected: weight,height as positive numbers (e.g. 70,1.75)")
    else:
        print("BMI:", result)

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    if result is None:
        print("Invalid input. Expected: non-negative whole numbers separated by spaces")
    else:
        print("Average Minutes:", result)


if __name__ == "__main__":
    main()