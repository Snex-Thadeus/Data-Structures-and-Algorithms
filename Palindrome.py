# A palindrome is a string which is same read forward or backwards.
# To write the program we need to follow three steps.
# 1. Take input
# 2. reverse the input
# 3. compare input and reversed input
# string[start:stop:step] string[::-1]--Reverses a string
number = int(input("Enter the Number:"))
string = str(number)
rev_string = string[::-1]
if string == rev_string:
    print("Number is Palindrome")
else:
    print("Number is not palindrome")