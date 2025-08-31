# Question 18
def task18_convert_minutes_to_hours(minutes):
    """
    Task 18:
    Write a function that accepts minutes as input
    and converts it into hours and minutes.
    Example: 130 minutes → "2 hour(s) 10 minute(s)"
    """
    hours = minutes // 60
    mins  = minutes % 60
    return f"{hours} hour(s) {mins} minutes(s)"

print(task18_convert_minutes_to_hours(130)) # 2 hour(s) 10 minute(s)

