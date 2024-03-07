student_name = input()
current_grade = 1
total_grades = 0
excluded = False
exclusion_grade = 0

while current_grade <= 12:
    grade = float(input())

    if grade >= 4:
        total_grades += grade
        current_grade += 1
    else:
        exclusion_grade+=1
        if exclusion_grade > 1:
            exclusion_grade = current_grade
            excluded = True
            break

if not excluded:
    average_grade = total_grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {exclusion_grade} grade")
