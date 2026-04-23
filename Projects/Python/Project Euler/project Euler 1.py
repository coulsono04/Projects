
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 2, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


numbers = []
number = 0
while number < 999:
    number = number + 1
    print(number)
    if number % 3 == 0:
        numbers.append(number)

print(numbers)

number = 0
while number < 999:
    number = number + 1
    print(number)
    if number % 5 == 0:
        numbers.append(number)

print(numbers)

total = 0

numbers = set(numbers)
print(numbers)

for num in numbers:
    total = total + num

print(total)