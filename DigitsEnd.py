number = int(input("Enter a five-digit integer: "))


if number < 10000 or number > 99999:
    print("That's not a five-digit number.")
else:
    
    divisor = 10000

   
    while divisor >= 1:
        digit = number // divisor        
        print(digit, end='  ')           
        number = number % divisor        
        divisor = divisor // 10          