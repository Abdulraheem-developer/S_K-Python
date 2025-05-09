
num1 = int(input("Enter a number: "))
# Set the largest and second largest values
largest = num1
second_largest = None

for i in range(9):
    num = int(input("Enter a number: "))

    if num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None or num > second_largest:
        if num != largest:
            second_largest = num


print("The largest number is:", largest)
print("The second largest number is:", second_largest)
