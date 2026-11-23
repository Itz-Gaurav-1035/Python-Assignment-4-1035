def total_sum(*args):
    print("Arguments received:", args)
    return sum(args)

print("Sum 1:", total_sum(10, 20))
print("Sum 2:", total_sum(5, 15, 25, 35))