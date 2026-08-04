import numpy as np
data=np.genfromtxt('student_marks.csv',delimiter=',')
slice_data=data[1:,3:]
print(slice_data)
math_marks=slice_data[::,:1]
print(math_marks)
max_number=np.max(math_marks)
print("Maximum math mark:", max_number)
min_number=np.min(math_marks)
print("Minimum math mark:", min_number)
mean_number=np.mean(math_marks)
print("Mean math mark:", mean_number)
average_math_marks=np.average(math_marks)
print("Average math mark:", average_math_marks)
standard_deviation=np.std(math_marks)
print("Standard deviation of math marks:", standard_deviation)
