#Program to Convert list of integers to a single integer

list=[11,22,33]
str1=''
for x in list:
	str1+=str(x);

z=int(str1);
print(z);