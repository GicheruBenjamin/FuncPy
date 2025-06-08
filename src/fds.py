
#Lists: Lists in Python are not strictly immutable, but they can be used in a functional way. For example, you can use list comprehensions to create new lists based on existing lists, without modifying the original list.
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  

#Tuples: Tuples are immutable sequences, similar to lists. Once a tuple is created, you cannot change its elements.
fruits = ('apple', 'banana', 'cherry')
print(fruits[0])  

#Sets: Sets are unordered collections of unique elements. They are immutable if created using the frozenset() function.
numbers = frozenset([1, 2, 3, 4, 5])
print(numbers)  

#Dictionaries: Dictionaries are mutable, but you can use the dict() function to create a new dictionary based on an existing one, without modifying the original.
person = {'name': 'John', 'age': 30}
new_person = dict(person, age=31)
print(new_person)  


