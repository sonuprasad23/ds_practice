# day05/grade_calculator.py
try:
    score_str = input("Enter the score (0-100): ")
    score = int(score_str)

    if score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
except ValueError:
    print("Invalid input. Please enter an integer score.")