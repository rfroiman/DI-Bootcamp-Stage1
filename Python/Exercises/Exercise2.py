# Ask the user for the human years
humanYears = int(input("Enter the human years: "))

# Calculate cat years
if humanYears == 1:
    catYears = 15
elif humanYears == 2:
    catYears = 24
else:
    catYears = 24 + (humanYears - 2) * 4

# Calculate dog years
if humanYears == 1:
    dogYears = 15
elif humanYears == 2:
    dogYears = 24
else:
    dogYears = 24 + (humanYears - 2) * 5

# Print the result
print([humanYears, catYears, dogYears])