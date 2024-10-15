def evaluate_grade(grade):
    if grade >= 5.5:
        return "Excellent!"

grade = float(input())
result = evaluate_grade(grade)

if result is not None:
    print(result)
