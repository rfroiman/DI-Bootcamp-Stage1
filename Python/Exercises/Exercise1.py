# ==========================================
# Exercise 1
# Declare a variable called first and assign "Hello World"
# ==========================================

first = "Hello World"


# ==========================================
# Exercise 2
# Write a comment that says: "This is a comment."
# ==========================================

# This is a comment.


# ==========================================
# Exercise 3
# Print "I AM A COMPUTER!"
# ==========================================

print("I AM A COMPUTER!")


# ==========================================
# Exercise 4
# If 1 < 2 and 4 > 2, print "Math is fun."
# ==========================================

if 1 < 2 and 4 > 2:
    print("Math is fun.")


# ==========================================
# Exercise 5
# Assign a variable called nope to an absence of value
# ==========================================

nope = None


# ==========================================
# Exercise 6
# Combine True and False using the "and" operator
# ==========================================

print(True and False)


# ==========================================
# Exercise 7
# Calculate the length of "What's my length?"
# ==========================================

print(len("What's my length?"))


# ==========================================
# Exercise 8
# Convert "i am shouting" to uppercase
# ==========================================

print("i am shouting".upper())


# ==========================================
# Exercise 9
# Convert the string "1000" to the number 1000
# ==========================================

print(int("1000"))


# ==========================================
# Exercise 10
# Combine the number 4 with the string "real"
# to produce "4real"
# ==========================================

print(str(4) + "real")


# ==========================================
# Exercise 11
# Record the output of 3 * "cool"
# ==========================================

print(3 * "cool")


# ==========================================
# Exercise 12
# Record the output of 1 / 0
# ==========================================

try:
    print(1 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")


# ==========================================
# Exercise 13
# Determine the type of []
# ==========================================

print(type([]))


# ==========================================
# Exercise 14
# Ask the user for their name
# ==========================================

name = input("What is your name? ")
print("Hello,", name)


# ==========================================
# Exercise 15
# Ask the user for a number and compare it to zero
# ==========================================

number = float(input("Enter a number: "))

if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")


# ==========================================
# Exercise 16
# Find the index of "l" in "apple"
# ==========================================

print("apple".index("l"))


# ==========================================
# Exercise 17
# Check whether "y" is in "xylophone"
# ==========================================

print("y" in "xylophone")


# ==========================================
# Exercise 18
# Check whether my_string is all lowercase
# ==========================================

my_string = "this is lowercase"
print(my_string.islower())