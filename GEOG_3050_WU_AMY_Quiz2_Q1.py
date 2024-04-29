# Question 1:
# Create a script that examines a string for the occurrence of a particular letter

mystr=input('Enter a string: ')
letter=input('Enter a letter: ')
print('This script will determine if your specified letter appears \nin your specified string:')

for i in mystr:
    if i==letter:
        in_str = 'YES'
        break
    else:
        in_str='NO'
print(in_str)
