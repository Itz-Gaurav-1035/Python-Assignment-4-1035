def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower

text = input("Enter a string: ")
u, l = count_case(text)
print("Uppercase count:", u)
print("Lowercase count:", l)