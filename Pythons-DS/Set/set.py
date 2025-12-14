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
