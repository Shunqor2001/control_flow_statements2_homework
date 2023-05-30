def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if 1==number:
        return "Monday"
    elif 2==number:
        return "Tuesday"
    elif 3==number:
        return "Wednesday"
    elif 4==number:
        return "Thursday"
    elif 5==number:
        return "Friday"
    elif 6==number:
        return "Saturday"
    elif 7==number:
        return "Sunday"
print(main(6))