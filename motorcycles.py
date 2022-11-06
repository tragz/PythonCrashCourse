motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Updateing the list element
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list
# append() method adds list element to the end of list without effecting other elements of the list.
# append() method adds list element to the end of list without effecting other elements of the list.
# append() method adds list element to the end of list without effecting other elements of the list.
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# insert elements into a List i.e adding a new element at any position in your list by using insert()
# imsert() method OPENS a space at position and stores the value at that location
# insert() method SHIFTS every other value in the list one position to the right
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing an item using the del statment
del motorcycles[0]
print(motorcycles)
print(motorcycles[0])

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")


first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")
print(motorcycles)

# Removing an item by value
# remove() method deletes only the first occurrence of the value you specify
motorcycles.remove('yamaha')
print(motorcycles)


