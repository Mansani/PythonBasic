# Grade Checker

# Take input from the user
score = int(input("Enter your score: "))

# Check the grade using if-else statements
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Output the result
print("Your grade is:", grade)
