
num1 = int(input("Enter first integer: "))

# Initialize sum, product, min, and max with the first number
total = num1
product = num1
smallest = num1
largest = num1


for i in range(3):
    num = int(input("Enter next integer: "))
    
    total += num
    product *= num

    if num < smallest:
        smallest = num
    if num > largest:
        largest = num


average = total / 4

# Display the results
print("Sum:", total)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)
