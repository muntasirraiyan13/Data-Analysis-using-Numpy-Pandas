import pandas as pd
df=pd.read_csv('student_marks.csv')
print(df)
math_marks=df['Maths']
print(math_marks)
date_of_birth=df['DOB']
print(date_of_birth)
