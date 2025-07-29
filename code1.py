def add(a, b):
    def try_convert_to_number(value):
        """Try to convert a value to a number (int or float), return None if not possible"""
        if isinstance(value, (int, float)):
            return value
        
        if isinstance(value, str):
            # Handle empty strings
            if value == "":
                return None
            
            # Try to convert to int first
            try:
                return int(value)
            except ValueError:
                pass
            
            # Try to convert to float (handles scientific notation, inf, nan)
            try:
                return float(value)
            except ValueError:
                pass
        
        return None
    
    # Handle special cases that should raise exceptions
    if a is None or b is None:
        # None doesn't have the expected behavior for string operations
        raise AttributeError("'NoneType' object has no attribute needed for addition")
    
    if isinstance(a, list) or isinstance(b, list):
        # Lists can't be meaningfully added to numbers
        raise TypeError("unsupported operand type(s) for +: 'list' and other types")
    
    # Try to convert both values to numbers
    num_a = try_convert_to_number(a)
    num_b = try_convert_to_number(b)
    
    # If both can be converted to numbers, perform arithmetic addition
    if num_a is not None and num_b is not None:
        result = num_a + num_b
        print(result)
        return result
    
    # Otherwise, perform string concatenation
    str_a = str(a) if a is not None else ""
    str_b = str(b) if b is not None else ""
    result = str_a + str_b
    print(result)
    return result