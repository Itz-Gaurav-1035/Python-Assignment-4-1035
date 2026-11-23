def largest_in_list(lst):
    largest = lst[0]
    for item in lst:
        if item > largest:
            largest = item
    return largest

nums = [14, 72, 35, 91, 28]
print("Largest element:", largest_in_list(nums))