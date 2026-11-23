# User-defined module for Q49 (imported in Q49.py)
def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage
