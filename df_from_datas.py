import pandas as pd
my_list=[['Raiyan',27],['Nuzhat',18],['Priyo',21],['Nishat',24]]
list=pd.DataFrame(my_list)
print(list) 

list1=[['Raiyan',20],['Nuzhat',20],['Priyo',21],['Nishat',21]]
df=pd.DataFrame(list1,columns=['Name','Age'])
print(df)

my_dict={
    'Name':['Raiyan','Nuzhat','Priyo','Nishat'],
    'Age':[27,18,21,24],
    'Gender':['Male','Female','Male','Female']
}
df=pd.DataFrame(my_dict)
print(df)

