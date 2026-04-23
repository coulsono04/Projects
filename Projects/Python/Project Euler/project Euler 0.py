
# Among the first 712 thousand square numbers, what is the sum of all the odd squares?


sqaureNumbers = []
squared = 0
time = 0
for i in range(1, 712000):
    number = i * i
    if number % 2 == 1:
        sqaureNumbers.append(number)

answer = 0
for number in sqaureNumbers:
    answer = answer + number

print(answer)