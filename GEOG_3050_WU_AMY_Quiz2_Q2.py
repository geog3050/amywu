# Question 2:
# Create a script that examines a list of numbers (for example, 2, 8, 64, 16, 32, 4)
# and determines the second-largest number.

print('This script determines the second-largest number in your list')

my_numbers = input('Enter a list of numbers, separated by spaces: ')

my_numbers = my_numbers.strip()
my_numbers = my_numbers.split()

as_list = [0]*len(my_numbers)
for i in range(len(my_numbers)):
    as_list[i]=int(my_numbers[i])

print(type(as_list))
as_list.sort()
scnd_larg = as_list[-2]
print(scnd_larg)

