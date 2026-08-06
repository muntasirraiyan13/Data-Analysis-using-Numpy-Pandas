import pandas as pd
df=pd.read_csv('student_marks.csv')
print(df)
df['DOB'] = pd.to_datetime(df['DOB'],format='%d-%m-%Y')
print(df['DOB'])
df['Year']=df['DOB'].dt.year
df['Month']=df['DOB'].dt.month
print(df['Year'])
print(df['Month'])