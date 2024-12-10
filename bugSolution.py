import math
def function_with_improved_error_handling(a, b):
    if a == 0:
        return float('inf') # Return positive infinity instead of crashing
    elif b < 0 and not isinstance(a, int):
        return math.pow(a,b) #Using math.pow for safer handling of floats with negative powers
    elif b < 0:
        if a==0:
            return float('inf')
        elif a<0 and not (b%2==0):
            return -((-a)**b)
        else:
            return a ** b
    return a + b