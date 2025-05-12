num_students = int(input('Enter number of students: '))

highest_score = -1
second_highest = -1
top_student = ""
second_student = ""

for i in range(num_students):
    name = input(f'Enter the name of student {i + 1}: ')
    score = float(input(f'Enter the score of {name}: '))

    if score > highest_score:
      
        second_highest = highest_score
        second_student = top_student

        highest_score = score
        top_student = name

    elif score > second_highest and score < highest_score:
        second_highest = score
        second_student = name

print(f'The student with the highest score is {top_student} with a score of {highest_score}.')
if second_highest != -1:
    print(f'The student with the second highest score is {second_student} with a score of {second_highest}.')
else:
    print('There is no second highest score.')
