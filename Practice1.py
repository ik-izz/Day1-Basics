import math


#initialize variable x to hello world then print out part of the string
x = 'hello world'
print(x[:5])

#reverses the string then prints it out
reverse = x[::-1]
print(f'string reversed is: {reverse}')

#Asks user for input then stores it in Y 
y = input('Enter you name: ')[::-1]
#reverses the string in Y and stores it in reverseY

#prints user input in reverse
print(f'Your name in reverse is: {y}')

#prints out the variable types
print(type(f'variable \'x\' type is:{x}'))
print(type(f'variable \'y\' type is:{y}'))
print(type(f'variable \'reverse\' type is:{reverse}'))

a = 5
b = 25
#adds a and b
print(f'adding a and b = {a + b}')

#finds the squareroot of b
print(math.sqrt(b))

#divides the variables then prints out the whole number without remainder
print(b//2)
print(b//3)
print(b//4)
print(b//5)
print(b//6)

#creates 2 lists
my_list = ['1' , 2]
my_list2 = [3, 4]

#prints combined lists
print(my_list + my_list2)

import array
list1 = (0, 1, 2)
list2 = (3, 4,5)
print(list1 + list2)

#covnerts and prints
print(ord('A'))
print(chr(65))
c = '51'
print(float(a))
print(float(c))
print(int(c))

#converts string in x to uppercase
print(x.upper())

py = 'Python'
for letter in py:
  print(letter)
#prints one object of the list 
print(my_list[1])

import sys
print('Python Version')
print(sys.version)
print(sys.version_info)
