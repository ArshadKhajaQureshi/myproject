# data type: List , It is used store multiple items in a single variable
#mutable example
fruits=["apple", 2 ,3]
x,y,z=fruits

print(type(fruits))

# list items are ordered, changeable , and allows duplicate values
# List items are indexed
# if we add new items it will be added at the end of the list
# list is mutable so we can add or delete the items or we can update a item

print(len(fruits))

tuple1=(23, 34,45,"True")

my_list=list((23, 34,45,"True"))
print(my_list)

my_list=list(tuple1)
print(my_list)

print(my_list[0])

print(my_list[0:3])
print("the id of my_list")
print(id(my_list))


my_list[1:4]=[95,96,97]
print(my_list)
print("the id of my_list")
print(id(my_list))


my_list[1:3]=[15,66,99]
print(my_list)

my_list[1:3]=["Cherry"]
print(my_list)
print("the id of whole my_list")
print(id(my_list))

c_list=my_list+fruits
print(c_list)


sliced_list=my_list[1:3]
print(id(sliced_list))
print(id(my_list[1:3]))

my_list.append("orange")
print(my_list)

print(my_list[1:-1])

for i in range(1,3):
    print(my_list[i])

my_list[1]="python"    #updating an element
print(my_list)

my_list.insert(1,"awesome") #inserting a new element and all the other elements on the R.H.S gets shifted to the RHS
print(my_list)

a=[1,2,3,4]
b=[5,6,7,8,9]
print("merged list")

a.extend(b)    #appending elements from another list to the current list
print(a)
print(b)

my_numbers=[12,11,10,9,8,7,6,5,4]
my_numbers.sort()
print(my_numbers)

# a is now [1, 2, 3, 4, 5, 6, 7, 8, 9]
a.remove(a[0])
print(a)

print("max value", max(a))
print("min value",min(a))

if(4 in a):
    print(" present")
else:
    print('not present')    

print(a[:4])

print(a[3:])

print(a)
a.reverse()
print(a)

nested_list=[[1,2,3],[4,5,6],[7,8,9]]

print(nested_list[0][0]) #accessing an element in the sublist

print(nested_list[1:3])

print(nested_list[0][1:3])

nested_list[1][1]=89
print(nested_list)

nested_list[2]=[23,23]
print(nested_list)

nested_list.append([13,14])
print(nested_list)

del nested_list[1]
print(nested_list)

nested_list[0].append(45)
print(nested_list)
x=list()

#iterate through the nested list
for i in nested_list:
    print(i)

for sublist in nested_list:
    for element in sublist:  
        print(element, end='  ')  

print(13*"*")
z=[11, 22, 13, 4, 5, 6, 7, 8, 19]
z.sort(reverse=True)
print(z)