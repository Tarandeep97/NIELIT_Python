#Using dict constructor
list=["Black","Red","Maroon","Yellow"]
list1=["#000000","#FF0000","#800000","#FFFF00"]
color_dict=dict(zip(list,list1))
print(color_dict)

#Using dictionary comprehensions

color_dict= {key:value for key, value in zip(list, list2)}


