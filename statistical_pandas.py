import pandas as pd
df=pd.read_csv('student_marks.csv')
print(df)
male_students=df.loc[df['Gender']=='M']
print("Total male:\n",len(male_students))
female_students=df.loc[df['Gender']=='F']
print("Total male:\n",len(female_students))

max_marks_math=df['Maths'].max()
mean_marks_math=df['Maths'].mean()
lowest_marks_math=df['Maths'].min()
total_marks_math=df['Maths'].sum()
highest_frequency_math=df['Maths'].mode()
number_of_failed_students=df.loc[(df['Maths']<33)|(df['Physics']<33)|(df['Chemistry']<33)|(df['English']<33)|(df['Biology']<33)|(df['Economics']<33)|(df['History']<33)|(df['Civics']<33)]
print("Maximm marks of math=",max_marks_math)
print("Average marks of math=",mean_marks_math)
print("Lowest marks of math=",lowest_marks_math)
print("Total marks of math=",total_marks_math)
print("The highest repeated marks in math:",highest_frequency_math)
print("The failed students are given below:\n",number_of_failed_students)
print("The number of failed students:\n",len(number_of_failed_students))


