def divisible_by_ten(num):
    
    remainder = num % 10
    
    # Use an if statement to check if the remainder is 0
    if remainder == 0:
        return True
    else:
        return False

# Test the function
print(divisible_by_ten(20))  
print(divisible_by_ten(25))  
