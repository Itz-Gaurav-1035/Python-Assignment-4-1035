x = "Global X"

def test_scope():
    x = "Local X"
    print("Inside function :", x)

test_scope()
print("Outside function:", x)