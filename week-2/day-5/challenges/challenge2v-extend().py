# adds the specified list elements to the end of the current list.
# in this example, adds car list to the end of the fruits list.

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

# output: ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

cars.extend(fruits)
print(cars)

# output: ['Ford', 'BMW', 'Volvo', 'apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']