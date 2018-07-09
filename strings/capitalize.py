#This Code inputs a string and prints string with each words first character in caps.
string = input()  
print(' '.join(i.capitalize() for i in string.split(" ")))
