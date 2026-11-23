def find_greatest(a, b, c):
    if a >= b and a >= c:
        print("Greatest number:", a)
    elif b >= a and b >= c:
        print("Greatest number:", b)
    else:
        print("Greatest number:", c)

find_greatest(18, 42, 29)