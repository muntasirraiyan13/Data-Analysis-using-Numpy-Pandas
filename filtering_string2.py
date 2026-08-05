import pandas as pd
data={
    'Name':['Mridul','Sourav','Nuzhat','Shuvo','Rabiul','Nur','Orko','Bithe','Bijoy','Raiyan'],
    'Roll':[1,3,4,5,7,8,9,10,11,13],
    'Gender':['M','M','F','M','M','M','M','F','M','M'],
    'Home_town':['Kurigram','Madaripur','Pabna','Nilphamari','Lalmonirhat','Kurigram','Pirojpur','Dhaka','Chandpur','Gaibandha']

}
df=pd.DataFrame(data)
print(df)
filtered=df.loc[df['Name'].str.contains("B")]
print("The name starts with B:\n",filtered)
