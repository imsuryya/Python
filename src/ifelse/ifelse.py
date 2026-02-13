marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter between 0 and 100.")

elif marks >= 90:
    print("Grade: A+")
    print("Excellent Performance!")

elif marks >= 75:
    print("Grade: A")
    print("Very Good!")

elif marks >= 60:
    print("Grade: B")
    print("Good!")

elif marks >= 40:
    print("Grade: C")
    print("You Passed.")

else:
    print("Grade: F")
    print("You Failed. Better luck next time!")