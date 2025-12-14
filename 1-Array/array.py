# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# List Functions: append | extend | insert | remove | pop | clear | count | index | sort | 
# reverse | copy

fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'banana']

# The append() method appends an element to the end of the list.
fruits.append("kiwi")

# The insert() method inserts the specified value at the specified position.
fruits.insert(1, "orange")

# The copy() method returns a copy of the specified list.
fruits_copy = fruits.copy()

# The index() method returns the position at the first occurrence of the specified value.
x = fruits.index("pear")

# The count() method returns the number of elements with the specified value.
x = fruits.count("apple")

# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print('Extended List: ', fruits)

# The reverse() method reverses the sorting order of the elements.
cars.reverse()
print('Reversed List', cars)

# The sort() method sorts the list ascending by default.
# reverse=True will sort the list descending. Default is reverse=False
cars.sort(reverse=True)
print('Sorted List', cars)

# The pop() method removes the element at the specified position
fruits.pop(1)   # default value is -1, which returns the last item

# The remove() method removes the first occurrence of the element with the specified value.
fruits.remove("orange")

# The clear() method removes all the elements from a list.
cars.clear()

# Compact Arrays [Efficient arrays of numeric values] using array module
import array

# Referencial Arrays
data = [ [22, 18, 709, 5, 33], [45, 32, 830, 120, 750], [4, 880, 45, 66, 61] ]
data = [0] * 4












































































