#!/usr/bin/python
#

import re
pattern = re.compile(r"")
my_string = input("Enter a string: ")
pattern = re.compile(r"[\D]+")
result = pattern.sub("_", my_string)

print("Modified string:", result)
print("Original string entered:", my_string)