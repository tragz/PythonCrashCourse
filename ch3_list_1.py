
# Adding elements to list
# append() method adds element at the last of the list
# insert(idx) method add element at idx location in the list and shifts elements

# Removing elments from a list
# pop() method - remove last elements
# remove(value) method - remove list element by value
# del statment[idx] - remove the item by idx


invites = ['God', 'GBR', 'Krishna', 'anasuya']

print("I am inviting your " + invites[0].title() + " to my place.")
print("I am inviting your " + invites[1].title() + " to my place.")
print("I am inviting your " + invites[2].title() + " to my place.")
print("I am inviting your " + invites[3].title() + " to my place.")



print("I am inviting your " + invites[-4].title() + " to my place.")
print("I am inviting your " + invites[-1].title() + " to my place.")
print("I am inviting your " + invites[-2].title() + " to my place.")
print("I am inviting your " + invites[-3].title() + " to my place.")

print(invites)

notVisiting = invites.remove('Krishna')
print(invites)

newVisitor = invites.insert(1 , 'Ganesh')
print(invites)


# use insert() method to add invite at the beginning of list
print("Inserting Jayant at the beginning of the list")
invites.insert(0, 'Jayant')
print(invites)

# use insert() method to add guest in the middle of your list
print("Inserting Adheip in between of the list")
invites.insert(3, 'Adheip')
print(invites)

#user append() method to add guest at the end of the list
print("Inserting Vishnu at the end of the list")
invites.append('vishnu')
print(invites)

print("List of Invites/Guest")
print(invites)
print("Sorry we cannot invitie you this time, " + invites.pop().title())
print(invites)
print("Sorry we cannot invitie you this time, " + invites.pop().title())
print(invites)
print("Sorry we cannot invitie you this time, " + invites.pop().title())
print(invites)
print("Sorry we cannot invitie you this time, " + invites.pop().title())
print(invites)
print("Sorry we cannot invitie you this time, " + invites.pop().title())
print("List of remaining Guest/Invites")
print(invites)

del invites[0]
print(invites)
del invites[0]
print(invites)




