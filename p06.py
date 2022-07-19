# Python program for Logical operator
# By : Pranav Visavadia
'''
(and) logical AND operator
(or) logical OR operator
(not) logical NOT operator
'''

a = True
b = True
c = False

# AND operator
if(a and b):
    print("This condition is true because a and b both are true.")

# OR operator
if(a or c):
    print("This condition is true because a is true and b is false.")

# NOT operator
if(not(c)):
    print("This condition is true because c is false and (not(c)) expression is true.")
