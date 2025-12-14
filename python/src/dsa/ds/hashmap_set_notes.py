# Python dictionary is used to implement Map DS.
# Function List: items | keys | values | copy | update | pop | popitem |
# get | setdefault | clear | fromkeys

dict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

# The items() method returns a list containing a tuple for each key value pair
print("Key Value Pair: ")
for item in dict.items():
    print(item)

# The keys() method returns a list containing the dictionary's keys
print("All Keys of Dictionary:")
for key in dict.keys():
    print(key)

# The values() method returns a list of all the values in the dictionary
print("All Values of Dictionary:")
for value in dict.values():
    print(value)

# The copy() method returns a copy of the specified dictionary.
dictCopy = dict.copy()

# The update() method inserts the specified items to the dictionary.
dict.update({"dummy1": "Hello"})
print("Actual Dictionary: ", dict)
dictCopy["dummy"] = 100
print("Copied Dictionary: ", dictCopy)

# The pop() method removes the specified item from the dictionary. A default value is optional as second parameter
print("Pop item: ", dictCopy.pop("dummy"))
print("Pop item: ", dictCopy.pop("dummy2", "Not Found"))

# The popitem() method removes the item that was last inserted into the dictionary.
dictCopy["dummy2"] = 100
print("Last Inserted Item: ", dictCopy.popitem())

# The get() method returns the value of the item with the specified key.
# Optional. A value to return if the specified key does not exist. Default value None
print(dictCopy.get("brand"))
print(dictCopy.get("transmission"))
print(dictCopy.get("transmission", "auto"))

# The setdefault() method returns the value of the item with the specified key.
# A default value is optional as second parameter
print("Value of Brand: ", dictCopy.setdefault("brand", "Ferrari"))
print("Copied Dictionary: ", dictCopy)

# The clear() method removes all the elements from a dictionary.
dict.clear()
print(dict)


# The fromkeys() method returns a dictionary with the specified keys and the specified value.
# It can be use to form a dictionary by combining two list or tuple
x = ("key1", "key2", "key3")
y = (0, 1, 2)

dict = dict.fromkeys(x, y)
print(dict)

x = ["key1", "key2", "key3"]
y = 1

dict = dict.fromkeys(x, y)
print(dict)


# A set is an unordered collection of items.
# Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# Function List: add | copy | discard | remove | pop | clear | union | update
# difference | difference_update | intersection | intersection_update | symmetric_difference |
# symmetric_difference_update |

fruits = {"apple", "banana", "cherry", "dummy1", "dummy2", "dummy3"}

# The add() method adds an element to the set.
fruits.add("orange")

# The copy() method copies the set.
x = fruits.copy()

# The discard() method removes the specified item from the set.
# The remove() method will raise an error if the specified item does not exist, and the discard() method will not.
x.discard("dummy1")
x.remove("dummy2")  # Raises an error if not found

# The pop() method removes a random item from the set.
print("Random Item: ", x.pop())

# The clear() method removes all elements in a set.
fruits.clear()
print(fruits)

# The union() method returns a set that contains all items from both sets, duplicates are excluded.
# We can specify as many sets we want, separated by commas. Ex: set.union(set1, set2...)
# The update() method updates the original set instead of returning a new set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)
x.update(y)

# The difference() method returns a set contains item that are present in set x, and not in set y.
# The difference_update() method updates the original set instead of returning a new set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
x.difference_update(y)
# Now the value of x & z is same.


# The intersection() method returns a set contains a mix of items that are present in both sets.
# The intersection_update() method updates the original set instead of returning a new set.
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)
x.intersection_update(y, z)
# Now the value of x & result is same.


# The symmetric_difference() method returns a set contains a mix of items that are not present
# in both sets. The symmetric_difference_update() method updates the original set instead of returning a new set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
x.symmetric_difference_update(y)
# Now the value of x & z is same.


# The isdisjoint() method returns True if no items in set x is present in set y, otherwise returns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

print("Two Sets are disjoint?: ", x.isdisjoint(y))

# The issubset() method returns True if all items in set x are present in set y, otherwise returns False.
print("X is subset of Y? : ", x.issubset(y))

# The issuperset() method returns True if all items set y are present in set x, otherwise returns False.
print("X is superset of Y?: ", x.issuperset(y))


# two implementations of a hash table, one using separate chaining and the other using open addressing with linear probing.

