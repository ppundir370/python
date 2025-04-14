num =int(input("Enter the number: "))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

res = factorial(num)
print("Factorial of num is :", res)
