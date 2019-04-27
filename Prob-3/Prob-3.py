# Module 3
#   Programming Assignment 4
#     Prob-3.py

# <YOUR NAME>

def letterGrade(score):
    # your code here
    if score < 2:
        grade = "F"
    elif score < 3:
        grade = "D"
    elif score < 4:
        grade = "C"
    elif score < 5:
        grade = "B"
    elif score >= 5:
        grade = "A"
    return grade

def unitTest():
    # your test code here
    print()
    for i in range(6):
        print("With a score of", i, "your letter grade is a", letterGrade(i))
    print()
if __name__ == "__main__":
    unitTest()