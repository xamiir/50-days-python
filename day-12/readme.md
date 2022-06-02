# Python Dictionaries

## Dictionary

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered\*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

Example
Create and print a dictionary:

`thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 } print(thisdict)`

# Accessing Items

You can access the items of a dictionary by referring to its key name, inside square brackets:

Example
Get the value of the "model" key:

`thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 } x = thisdict["model"]`

# Change Values

You can change the value of a specific item by referring to its key name:

## Example

`Change the "year" to 2018:`

`thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 } thisdict["year"] = 2018 `

# Adding Items

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

## Example

`thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 } thisdict["color"] = "red" print(thisdict)`

# Removing Items

There are several methods to remove items from a dictionary:

# Example

- The pop() method removes the item with the specified key name:

`thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 } thisdict.pop("model") print(thisdict)`

# Loop Through a Dictionary

You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

Example
Print all key names in the dictionary, one by one:

for x in thisdict:
print(x)

# Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.

Example
Create a dictionary that contain three dictionaries:

`myfamily = { "child1" : { "name" : "Emil", "year" : 2004 }, "child2" : { "name" : "Tobias", "year" : 2007 }, "child3" : { "name" : "Linus", "year" : 2011 } } `

# Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

- Method Description
- clear() Removes all the elements from the dictionary
- copy() Returns a copy of the dictionary
- fromkeys() Returns a dictionary with the specified keys and value
- get() Returns the value of the specified key
- items() Returns a list containing a tuple for each key value pair
- keys() Returns a list containing the dictionary's keys
- pop() Removes the element with the specified key
- popitem() Removes the last inserted key-value pair
- setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
- update() Updates the dictionary with the specified key-value pairs
- values() Returns a list of all the values in the dictionary
