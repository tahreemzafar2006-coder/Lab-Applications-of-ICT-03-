# Step 1: Take input from user
marks = int(input("Enter your marks (0-100):"))

# Step 2: Logical operations with if, elseif, else
if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 75 and marks < 90: # "and" ensure both conditions are True
    grade = "B"
elif marks >= 50 and marks < 75:
   grade = "C"
elif: # marks < 50 and marks > 0:
    grade = "F"
else:
    print("invalid input")
print("your grade is:", grade)
