counter = 10

def update_counter():
    global counter
    counter += 5
    print("Inside function after modification:", counter)

print("Before function call:", counter)
update_counter()
print("After function call :", counter)