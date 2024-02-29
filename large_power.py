def large_power(base, exponent):
    result = base ** exponent
    
    # Use an if statement to test if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Test the function
print(large_power(10, 3))  
print(large_power(10, 4))  
