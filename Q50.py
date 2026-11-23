# Main program importing modules from user-defined package: my_pkg
from my_pkg.mod_one import greet
from my_pkg.mod_two import double

print(greet("Gaurav"))
print("Double of 15:", double(15))