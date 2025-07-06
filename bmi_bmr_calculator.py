# Step 1: Collect user info
name = input("What's your name? ")
age = int(input("How old are you? "))
gender = input("What is your gender? (male/female): ").lower()
height_cm = float(input("Enter your height in cm: "))
weight_kg = float(input("Enter your weight in kg: "))

#input() collects user input.
#int() and float() convert strings to numbers.
#.lower() makes gender input easier to compare later (e.g., "Male" vs "male").

# Step 2: Calculate BMI
height_m = height_cm / 100  # convert cm to meters
bmi = weight_kg / (height_m ** 2)

# Classify the BMI
if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

print(f"\n{name}, your BMI is {bmi:.2f} which is considered {bmi_category}.")

#BMI formula: weight / height²
#Classification using if / elif / else
#:.2f formats BMI to 2 decimal places

# Step 3: Calculate BMR using Mifflin-St Jeor formula
if gender == "male":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
elif gender == "female":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
else:
    bmr = None  # fallback if gender is unknown

if bmr:
    print(f"Your estimated BMR is {bmr:.0f} calories/day.")
else:
    print("Invalid gender input. BMR could not be calculated.")
    
#Different formula for men and women
#Use if for logic branching
#Handle invalid gender gracefully

