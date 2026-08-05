import pandas as pd
data={
    'Name':['Mridul','Sourav','Nuzhat','Shuvo','Rabiul','Nur','Orko','Bithe','Bijoy','Raiyan'],
    'Roll':[1,3,4,5,7,8,9,10,11,13],
    'Gender':['M','M','F','M','M','M','M','F','M','M'],
    'Home_town':['Kurigram','Madaripur','Pabna','Nilphamari','Lalmonirhat','Kurigram','Pirojpur','Dhaka','Chandpur','Gaibandha']

}
df=pd.DataFrame(data)
print(df)
northern_districts_bd=['Panchagarh','Thakurgaon','Dinajpur','Nilphamari','Lalmonirhat','Rangpur','Kurigram','Gaibandha','Joypurhat','Bogura','Naogaon','Natore','Chapainawabganj','Rajshahi','Sirajganj','Pabna']
applicable_for_qouta=df.loc[df['Home_town'].isin(northern_districts_bd)]
print('These people are applicable for qouta:\n',applicable_for_qouta)

female=df.loc[df['Gender']=='F']
print("The female:\n",female)

