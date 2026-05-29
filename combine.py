"""Takes two lists from the user
● Converts them into sets
● Finds common elements between both sets
6."""
list=[]
list2=[]

for student in range(5) :
    _list=int(input("Enter number"))
    list.append(_list)
print(list)
for student in range(5) :
    _list=int(input("Enter number"))
    list2.append(_list)
print(list2)
print(set(list))
print(set(list2))


result=set(list).intersection(list2)
print(result)
