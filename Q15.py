def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is Even.")
    else:
        print(f"{n} is Odd.")

num = int(input("Enter an integer: "))
check_even_odd(num)