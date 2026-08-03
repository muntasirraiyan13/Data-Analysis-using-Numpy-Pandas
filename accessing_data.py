import pandas as pd
list=pd.read_csv('student_marks.csv')
print(list.describe())
# Accessing data from columns
print(list)
print(list['Gender'])
print(list['DOB'])
print(list['Maths'])
print(list['Biology'])
print(list.loc[0])
print(list.loc[[2,3,4]])