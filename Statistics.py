
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


numbers = [num1, num2, num3]


_sum = sum(numbers)
_average = _sum / 3
_product = num1 * num2 * num3
_smallest = min(numbers)
_largest = max(numbers)

print("Sum:", _sum)
print("Average:", _average)
print("Product:", _product)
print("Smallest:", _smallest)
print("Largest:", _largest)
