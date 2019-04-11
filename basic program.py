#Python Indentations
if 5 > 2:
  print("Five is greater than two!")
#Creating Variables
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
x = "awesome"
print("Python is " + x)
#Specify a Variable Type
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World!  "
print(a.strip()) # returns "Hello, World!"
#The len() method returns the length of a string:
a = "Hello, World!"
print(len(a))
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#Command-line String Input string should be given in "  "
x = input()
print("Hello, ", x)
#A list is a collection which is ordered and changeable.
thislist = ["apple", "banana", "cherry"]
print(thislist)
#To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#To add an item at the specified index, use the insert() method:
thislist.insert(1, "orange")
print(thislist)
#The remove() method removes the specified item:
thislist.remove("banana")
print(thislist)
#The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)
#The clear() method empties the list:
thislist.clear()
print(thislist)
#It is also possible to use the list() constructor to make a list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
#to add one item to a set use the add() method.
thisset.add("orange")
print(thisset)
#Add multiple items to a set, using the update() method:
thisset.update(["orange", "mango", "grapes"])
print(thisset)
#To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")
print(thisset)
# If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana")
print(thisset)
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
