height = 1.65
weight = 84

# Calculate the bmi using weight and height.
bmi = weight / height**2

# Rounding function
print(round(bmi))
print(round(bmi, 2))

# Increment methods
x = 1
x + 1
x += 1

# f-strings - to combine different data types
# Curly braces are used to place the variables 
print(f"My BMI is {round(bmi, 2)}")
