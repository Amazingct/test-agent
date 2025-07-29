def add(a,b):
  # Convert string inputs to numbers if possible
  a_converted = a
  b_converted = b
  
  if isinstance(a, str):
    try:
      # Try to convert to int first, then float if that fails
      # Check for float indicators: decimal point, scientific notation, inf, nan
      if '.' in a or 'e' in a.lower() or 'inf' in a.lower() or 'nan' in a.lower():
        a_converted = float(a)
      else:
        a_converted = int(a)
    except ValueError:
      # If conversion fails, keep as string
      a_converted = a
  
  if isinstance(b, str):
    try:
      # Try to convert to int first, then float if that fails
      # Check for float indicators: decimal point, scientific notation, inf, nan
      if '.' in b or 'e' in b.lower() or 'inf' in b.lower() or 'nan' in b.lower():
        b_converted = float(b)
      else:
        b_converted = int(b)
    except ValueError:
      # If conversion fails, keep as string
      b_converted = b
  
  # Handle mixed types: if one is string and other is number, convert number to string
  if isinstance(a_converted, str) and isinstance(b_converted, (int, float)):
    b_converted = str(b_converted)
  elif isinstance(b_converted, str) and isinstance(a_converted, (int, float)):
    a_converted = str(a_converted)
  
  print(a_converted + b_converted)

