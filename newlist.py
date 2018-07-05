def newList(list):
	"This function returns a new list with unique values from given list"
	new_list=[]
	new_list.append(list[0])
	for x in list:
		if x not in new_list:
			new_list.append(x)
		else:
			pass
	print(new_list)
	return;	