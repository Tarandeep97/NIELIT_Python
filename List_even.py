import random
list=[random.randint(1,100) for x in range(random.randint(5,10))]
#Random List
print(list)
for i in list:
	if i%2==0:
		list.remove(i);
#List without even no.s
print(list);