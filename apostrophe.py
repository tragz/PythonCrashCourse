message = "one of Python's strenths is its diverse community"
print(message)

'''
apostrophe - error 

message = 'one of Python's strenths is its diverse community'
print(message)

File "/Users/raghav.tanaji/Desktop/python_work/apostrophe.py", line 5
    message = 'one of Python's strenths is its diverse community'
                             ^
SyntaxError: invalid syntax

Interpresete  doesn't recognize somethign in the code as valid Python code
'''


age = 23
'''message = "Happy " + age + "rd Birthday!"'''
print(message)


message = "Happy " + str(age) + "rd Birthday!"
print(message)
