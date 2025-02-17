# Sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Get only even numbers from the list
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# 2. Get squares of each number in the list
squares = [num ** 2 for num in numbers]
print("Squares:", squares)

# 3. Get squares of even numbers only
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print("Even number squares:", even_squares)

# 4. Convert each number to a string with a prefix
str_numbers = [f"Number {num}" for num in numbers]
print("Number with prefix:", str_numbers)

# 5. Flatten a list of lists
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [element for row in matrix for element in row]
print("Flattened list:", flattened)

# 6. Get the squares of numbers that are divisible by 3
divisible_by_3_squares = [num ** 2 for num in numbers if num % 3 == 0]
print("Squares of numbers divisible by 3:", divisible_by_3_squares)
