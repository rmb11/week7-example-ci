def add(a, b):
    """
    Adds two values. 

    Parameters:
    a: int | float | str
        First operand.  
    b: int | float | str
        Second operand.  

    Returns:
    int | float | str
        Sum of "a" and "b". 
    
    Example
    >>> add(2, 3)
    5
    >>> add("space", "ship")
    'spaceship''
    """
    return a + b

def subtract(a, b):
    """
    Subtracts b from a.  

    Parameters:
    a: int | float 
        First operand.  
    b: int | float 
        Second operand.  

    Returns:
    int | float 
        Result of a - b
    
    Example
    >>> subtract(2, 3)
    -1
    >>> subtract(2, 1)
    1
    """
    return a - b  

def multiply(a, b):
    """
    Multiplies two values.

    Parameters:
    a: int | float
        First operand.  
    b: int | float
        Second operand.  

    Returns:
    int | float
        Product of a and b.

    Examples:
    >>> multiply(2, 3)
    6
    >>> multiply(3, 3)
    9
    """
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Converts fahrenheit to celsius.

    Parameters:
    fahrenheit: int | float
        Temperature in fahrenheit.

    Returns:
    float
        Temperature in celsius.

    Raises:
    AssertionError
        If temperature is below absolute zero (-459.67°F).

    Examples:
    >>> convert_fahrenheit_to_celsius(32)
    0.0
    >>> convert_fahrenheit_to_celsius(122)
    50.0
    """
    if fahrenheit < -459.67: 
        raise AssertionError("Temperature cannot be below absolute zero")
    return multiply(subtract(fahrenheit, 32), 5 / 9) 