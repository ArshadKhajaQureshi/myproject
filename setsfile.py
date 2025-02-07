# sets are used to store multiple items in a single variable
# Set items are unchangeable, but you can add or remove items
# sets are unordered, unindexed, doesnot allow duplicate values
# it is having curly brackets


thisset={"apple", "banana", "cherry"}
print(thisset)

thisset2={}
print(type(thisset2))

thisset3=set(("kiwi", "strawberry", "cherry"))

thisset.add("orange")
print(thisset)

thisset.update(thisset3)
print(thisset)

thisset.remove("banana")
print(thisset)

# thisset.remove("banana")
# print(thisset)

set1={"a","b","c"}

print("b" in set1)

set1.add("cherry")
print(set1)

set2={1,2,3}

set3=set1.union(set2)
print(set3)
#both update and union will remove duplicates

x={"apple","banana","cherry"}
y={"google","microsoft","apple"}

z=x.intersection(y)
print(z)  #returns a set that contains the items that exists in both set x and set y

x.symmetric_difference_update(y)  # x is getting updated and y doesnot change

print(x)
#it will keep only the elements that are not present in both the sets

z=x.symmetric_difference(y) #here x and y will not be affected
print(z)
print(y)
print(x)

z=x.difference(y)  
#the difference method returning a set that contains the difference between two 
# sets and the returned set contains the items thst exist only in the first

print(z)