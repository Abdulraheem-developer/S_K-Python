num_students = int(input('Enter number of students: '))

highest_score = -1
top_student = ""

for i in range(num_students):
    name = input(f'Enter the name of student {i + 1}: ')
    score = float(input(f'Enter the score of {name}: '))

    if score > highest_score:
        highest_score = score
        top_student = name

print(f'The student with the highest score is {top_student} with the score of {highest_score}.')


