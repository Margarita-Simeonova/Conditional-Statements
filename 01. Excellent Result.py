def evaluate_grade(grade):
    
    if grade >= 5.5:
        # return result
        return "Excellent!"

grade = float(input())

# take result
result = evaluate_grade(grade)

if result is not None:
    # if right result
    print(result)
