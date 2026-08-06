import pandas as pd
df=pd.read_csv('student_marks.csv')
print(df)
gender_group=df.groupby('Gender')
for gender, df_gen in gender_group:
    print(gender)
    print(df_gen)
a=gender_group.describe()
print(a)
