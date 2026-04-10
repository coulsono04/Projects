
# Decimal to Binary Calculator
list = []
number = 4321
print(number)
while number > 0:
    if number % 2 == 1:
        list.append(1)
    else:
        list.append(0)
    number = number // 2
    print(number)

print(list)
list.reverse()
print(list)

# Binary to Decimal

number = [1,1,0,0,1,1,1,0,0,0]
from_right = len(number) - 1
final_number = 0
print(from_right)
for num in number:
    num_to_add = num * 2 ** from_right
    final_number = final_number + num_to_add
    from_right -= 1
print(final_number)

# Binary to Oct

# number = [1,100,111,000]
# from_right = len(number) - 1
# final_number = 0
# print(from_right)
# for num in number:
#     num_to_add = num * 8 ** from_right
#     final_number = final_number + num_to_add
#     from_right -= 1
# print(final_number)