# tuples are immutable, ordered, allow duplicate values

fruits=("apple", "banana","cherry")

print(len(fruits))
print(type(fruits))


# Not a tuple
thistuple=("apple")
print(thistuple)
print(type(thistuple))

my_tuple=tuple(("myname","myaddr"))
print(type(my_tuple))

list2=[2,3,4,5,[23,45,56,78]]
my_listTuple=tuple(list2)
print(type(my_listTuple))
print(my_listTuple)

my_dict={"john":1,"jerry":2}
tupleDictionary=tuple(my_dict)
print(tupleDictionary)

fruits=("apple","banana","cherry")

newtuple=tupleDictionary+fruits
print(newtuple)

mytuple=(newtuple*4)
print(mytuple)

x=mytuple.count("john")
print(x)

y=mytuple.index("john")
print(y)

print(fruits[0])