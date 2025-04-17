'''
x = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,11):
    print(i)
numbers = list(range(1,11))
print(numbers)
'''  # <- CLOSE this comment block

numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers)

firstfive = numbers[0:5]
print(firstfive)

reversedNumbers = firstfive[::-1]
print(reversedNumbers)

