from math import *


def is_palindrome(number):
	number = str(number)
	inverse_number = number[::-1]	   
	number = int(number)
	inverse_number = int(inverse_number)
	if number == inverse_number:
		return True
	else: 
		return False

num = []
palindrome = []
for x in range(100,1000):
	for y in range(100,1000):
		num.append(x * y)

i = 1

while i < len(num):
	if is_palindrome(num[i]) == True:
		palindrome.append(num[i])
		i = i + 1
	else: 
		i = i + 1

print(max(palindrome))


