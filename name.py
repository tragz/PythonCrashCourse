name = "ada lovelace"
print(name.title())

'''
name.title() -> capitals the first letter of each word in the string
dot (.) after name in name.title() tells Pytnon to make the 
title() method act on variable name

methods is followed by set of parantheses - as it requires additional
info to do their work, that info is provided inside parantheses


'''

name = name.title()
print(name.upper())
print(name.lower())

'''
lower() method is useful for storing data
'''

'''
Combining or Concatenationg Strings

'''

first_name = "ada"
last_name = "lovelace"

full_name = first_name + " " + last_name

print(full_name)


print("Hello, " + full_name.title() + "!")


print("Python")
''' TAB'''
print("\tPython") 
''' NeW Line'''
print("Languages:\nPython\nC\nJavaScript") 
print("Languages:\n\tPython\n\tC\n\tJavaScript") 

'''Stripping Whitespace'''

favorite_language = 'python '

print(favorite_language + "End")

favorite_language = favorite_language.rstrip()

print(favorite_language + "End")

'''
rstrip - strip from righ
lstrip - strip from left
'''






