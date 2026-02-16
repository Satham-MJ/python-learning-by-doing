# Learning about string by doing

name="Satham Ussain"
description="""FullStack Developer
Skills: Javascript, React, Node, php
Locaiton : Remote """

# Single and Multi line stirng
print(name)
print(description)

# string length

print(name," length ",len(name))

# Strings are array like other programming language

print(name[0])

# Looping through string
for x in name:
    print(x)

# check string has partuclar word

print("Node" in description)

# check string is there in condition

if "React" in description:
    print("React Developer")

if "AI" not in description:
    print("Not AI developer")