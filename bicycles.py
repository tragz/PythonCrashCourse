bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing individual elements in list
print(bicycles[0])

#Operation on list elements
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
# check off-by-one error
# Index start with 0, reason has to do with how list operations are implemented at a lower level
print(bicycles[1])
print(bicycles[3])

# Python has special syntax for accessing last element in a list
print(bicycles[-1])
# useful to access last element without knowing exactly how long the list is


# Using Individual values from a list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)