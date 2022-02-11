list1=[1,2,2,3,3,66,78,29,38,35,48]
list2=[]
for i in list1:
	if i not in list2:
		list2.append(i)
print(list2)