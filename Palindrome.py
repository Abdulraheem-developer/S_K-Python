number = int(input("Enter a five-digit number: "))


if number < 10000 or number > 99999:
    print("That's not a five-digit number.")
else:
    
    digit1 = number // 10000
    digit2 = (number // 1000) % 10
    digit3 = (number // 100) % 10
    digit4 = (number // 10) % 10
    digit5 = number % 10


    if digit1 == digit5 and digit2 == digit4:
        print("This number is a palindrome.")
    else:
        print("This number is not a palindrome.")
