# Lists
# fruits = ["apple", "mango", "avocado", "banana", "orange"]

# for fruit in fruits:
#     print(fruit)

# index = position of each item inside a list - starts counting from 0
# print(fruits[2])
# print(fruits[-4])

# lenght = number of items inside a List - starts counting from 1
# print(len(fruits))

#Dictionaries - key: value

fruits = {'apple':{'taste': 'sweet', 'shape': 'roundy', 'region':'Tropical'}, 'mango': {'whatever': 'text'}}

for item in fruits:
    print(item)
    print(fruits[item])
    print(fruits[item]['shape'])
