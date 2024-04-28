
#map(function, iterable): This function applies a function to every item of an iterable (e.g., list, tuple, etc.) and returns a map object (which is an iterator).
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#filter(function, iterable): This function constructs an iterator from elements of an iterable for which a function returns true.
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

#reduce(function, iterable): This function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  

#functools.partial(func, args, keywords): This function returns a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords.
from functools import partial
def multiply(x, y):
    return x * y
double = partial(multiply, 2)
print(double(5))  

#all(iterable): This function returns True if all elements of the iterable are true (or if the iterable is empty).
numbers = [1, 2, 3, 4, 5]
all_positive = all(number > 0 for number in numbers)
print(all_positive)  


#any(iterable): This function returns True if any element of the iterable is true. If the iterable is empty, returns False.
numbers = [0, 1, 2, 3, 4]
any_zero = any(number == 0 for number in numbers)
print(any_zero)  

#enumerate(iterable, start=0): This function returns an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

#zip(iterables): This function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'purple']
for fruit, color in zip(fruits, colors):
    print(fruit, color)


#reversed(seq): This function returns a reverse iterator. seq must be an object which has a reversed() method or supports the sequence protocol (the len() method and the getitem() method with integer arguments starting at 0).
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)  

#sorted: This function returns a new sorted list from the items in iterable.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  
