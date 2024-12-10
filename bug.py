def function_with_uncommon_error(a, b):
    if a == 0:
        return 1 / a  # ZeroDivisionError, but less common due to explicit check
    elif b < 0:
        return a ** b  # Negative exponent with non-integer base may cause issues
    return a + b