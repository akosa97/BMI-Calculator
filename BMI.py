# BMI Calculator

# Ask the user for their height in feet and inches
height_feet = int(input("Enter your height in feet: "))
height_inches = int(input("Enter your height in inches: "))

# Convert the height to inches and then to meters
height_total_inches = height_feet * 12 + height_inches
height_meters = height_total_inches * 0.0254

# Ask the user for their weight in pounds
weight_pounds = int(input("Enter your weight in pounds: "))

# Convert the weight to kilograms
weight_kg = weight_pounds * 0.453592

# Calculate the BMI
bmi = weight_kg / (height_meters ** 2)

# Print the BMI to the user
print("Your BMI is: ", round(bmi, 2))
