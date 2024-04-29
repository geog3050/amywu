# Create a script that examines a list of numbers
#(for example, 2, 8, 64, 16, 32, 4, 16, 8) to determine whether
# it contains duplicates. The script should print a meaningful result,
# such as “The list provided contains duplicate values” or “The list
# provided does not contain duplicate values.” An optional addition is to remove
# the duplicates from the list.
# HINT: You can use list.count(value) to determine how many occurrences
# of a value exists in a list. 

print('This script determines if your specified list contains duplicates')

my_numbers = input('Enter a list of numbers, separated by spaces: ')

my_numbers = my_numbers.strip()
my_numbers = my_numbers.split()

as_list = [0]*len(my_numbers)
for i in range(len(my_numbers)):
    as_list[i]=int(my_numbers[i])


set_version = set(as_list)
if len(as_list) == len(set_version):
    print('The list provided DOES NOT contain duplicate values')
else:
    print('The list provided contains duplicate values')
    print('Remove all duplicates: ', set_version)

