# Lists - are ordered, mutable sequence of items.
# dictionaries - are unorder colloections that store data as key-value pairs

#! examples

#! list
fruits = ['apple', 'strawberry', 'banana', 'kiwi']
print(fruits)

# built in methods - append(), remove(), sort(), pop(), and insert()

# add an item
fruits.append('orange')
print(fruits)

# remove item
fruits.remove('banana')
print(fruits)

# sort list
fruits.sort
print(fruits)

# nested lists - list of lists. this allows for "multi-dimensional" data storage
matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]

print(matrix[1][1])
print(matrix[0][2])
print(matrix[2][0])

#! dictionary
fruit_color = {'apple':'red', 'banana':'yellow', 'kiwi':'golden',}
print(fruit_color)

# dictionary methods
# accessing keys and values
keys = fruit_color.keys()
values = fruit_color.values()
print(keys)
print(values)

# update dictionary
fruit_color['apple'] = "green"
print(values)

# using get() to handle missing keys
print(fruit_color.get('orange', 'not found'))

fruit_color["orange"] = 'orange orange'
print(fruit_color)

fruit_color.update({"grapes":'purple'})
print(fruit_color)