# Main program importing user-defined module: marks_mod.py
import marks_mod

student_marks = [88, 92, 85, 90, 86]
total, percent = marks_mod.calculate_result(student_marks)

print("Total Marks:", total)
print(f"Percentage : {percent:.2f}%")