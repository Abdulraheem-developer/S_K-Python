import random

score = 0

for i in range(1, 11):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    if num1 < num2:
        num1, num2 = num2, num1

    correct_answer = num1 - num2
    print(f"\nQuestion {i}: What is {num1} - {num2}?")

    for attempt in range(1, 3):
        answer = int(input(f"Attempt {attempt}: "))
        if answer == correct_answer:
            print("Correct!")
            score += 1
            break
        else:
            print("Wrong.")
    
    if answer != correct_answer:
        print(f"The correct answer was {correct_answer}.")

print(f"\nQuiz Over! You got {score} out of 10 correct.")
