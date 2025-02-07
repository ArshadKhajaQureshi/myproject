# dictionaries is collection of ordered, changeable 

# the values in dictionaries can be of any data type
thisD={
    "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":2020,
    "colors":["red","white","blue"],
    (1,2):"tyre"
}
print(thisD)
print(thisD["brand"])

print(thisD.keys())

print(thisD.get("colors"))

# Adding key value pair inside dictionary
thisD["Headlightcolor"]="Green"

print(thisD)

print(thisD.values())

#chnaging the key value pair
thisD["brand"]="mercedes"
print(thisD)

#nested dictionary
myfamily={
  "child1":{
      "name":"emili",
      "year":2004
  },
   "child2":{
      "name":"Tabu",
      "year":2006
  },
   "child3":{
      "name":"Linus",
      "year":2012
  },

}

print(myfamily)

# other way of nesting

child1={
    "name":"emili",
      "years":[2004, 2011, 4]
}

child2={
    "name":"john",
      "years":[2004, 2011, 4]
}

child3={
    "name":"Johnny",
      "years":[2004, 2011, 4]
}

myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}

print("child1 name", myfamily['child1']['name'])

#iterating through all childrens
for child,details in myfamily.items():
    print(f"{child} Details: Name={details['name']} , Year={details["years"][0]}")