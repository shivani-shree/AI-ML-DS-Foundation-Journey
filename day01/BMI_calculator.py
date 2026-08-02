# BMI CALCULATOR
height = float(input("Enter height in metre: "))
weight = float(input("Enter weight in kg: "))

# BMI = weight(kg) / height(m)^2
BMI = weight / (height)**2

if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI < 25:
    category = "Normal"
elif 25 <= BMI < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {BMI:.2f} - Category: {category}")


