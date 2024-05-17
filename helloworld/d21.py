from functools import partial

# Example function that multiplies two numbers
def multiply(x, y):
    return x * y

# Create a new function that multiplies by 2 using partial
multiply_by_2 = partial(multiply, 2)

# Now we can use multiply_by_2 as a specialized function
result = multiply_by_2(5)  # This is equivalent to multiply(2, 5)
print(result)  # Output: 10
