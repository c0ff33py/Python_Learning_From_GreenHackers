# check_ranges.py

def in_range(value, min_value, max_value):
    """Check if a number falls within a range"""
    if isinstance(value, (int, float)):
        return min_value <= value <= max_value
    return False

def positive(value):
    """Check if a number is positive"""
    return isinstance(value, (int, float)) and value > 0

