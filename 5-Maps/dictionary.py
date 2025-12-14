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
