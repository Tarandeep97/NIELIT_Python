
#Program to sum all items in a list
import random
list=[random.randint(1,100) for x in range(random.randint(1,10))]
sum=0;
for i in range(1,len(list)):
	sum+=list[i];

	
print("sum of list",sum)
