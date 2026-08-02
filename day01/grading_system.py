# GRADING SYSTEM

marks = int(input("Enter your Marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks! Please enter a value between 0 and 100")
elif marks >= 90:
    print(f"Marks: {marks} -> Grade: A")
elif marks >= 80:
    print(f"Marks: {marks} -> Grade: B")
elif marks >= 70:
    print(f"Marks: {marks} -> Grade: C")
elif marks >= 60:
    print(f"Marks: {marks} -> Grade: D")
elif marks >= 40:
    print(f"Marks: {marks} -> Grade: E")
else:
    print(f"Marks: {marks} -> Grade: F")
 
    
