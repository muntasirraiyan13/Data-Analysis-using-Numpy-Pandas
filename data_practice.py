import pandas as pd
df=pd.read_csv('synthetic_nid_dataset.csv')
print(df)
blood_group=df.loc[df['Blood_Group']=='AB-']
blood_group_2=df.loc[df['Blood_Group']=='AB+']
blood_group_3=df.loc[df['Blood_Group']=='A+']
blood_group_4=df.loc[df['Blood_Group']=='B+']
blood_group_5=df.loc[df['Blood_Group']=='O+']
blood_group_6=df.loc[df['Blood_Group']=='O-']
blood_group_7=df.loc[df['Blood_Group']=='A-']
blood_group_8=df.loc[df['Blood_Group']=='B-']
print("These people are having AB- blood group:\n",blood_group)
print("These people are having AB+ blood group:\n",blood_group_2)
print("These people are having A+ blood group:\n",blood_group_3)
print("These people are having B+ blood group:\n",blood_group_4)
print("These people are having O+ blood group:\n",blood_group_5)
print("These people are having O- blood group:\n",blood_group_6)
print("These people are having A- blood group:\n",blood_group_7)
print("These people are having B- blood group:\n",blood_group_8)

print("The number of people having AB- blood group:\n",len(blood_group))
print("The number of people having AB+ blood group:\n",len(blood_group))
print("The number of people having A+ blood group:\n",len(blood_group))
print("The number of people having B+ blood group:\n",len(blood_group))
print("The number of people having O+ blood group:\n",len(blood_group))
print("The number of people having O- blood group:\n",len(blood_group))
print("The number of people having A- blood group:\n",len(blood_group))
print("The number of people having B- blood group:\n",len(blood_group))

male_people=df.loc[df['Gender']=='Male']
female_people=df.loc[df['Gender']=='Female']
print("Total number of male:\n",len(male_people))
print("Total number of female:\n",len(female_people))

single_people=df.loc[df['Marital_Status']=='Single']
married_people=df.loc[df['Marital_Status']=='Married']
divorced_people=df.loc[df['Marital_Status']=='Divorced']
print("The number of single people:\n",len(single_people))
print("The number of married people:\n",len(married_people))
print("The number of divorced people:\n",len(divorced_people))

living_in_dhaka=df.loc[df['District']=='Dhaka']
print("The people who are living in Dhaka:\n",len(living_in_dhaka))
living_in_gazipur=df.loc[df['District']=='Gazipur']
print("The people who are living in Gazipur:\n",len(living_in_gazipur))
living_in_narayanganj=df.loc[df['District']=='Narayanganj']
print("The people who are living in Narayanganj:\n",len(living_in_narayanganj))

doctor=df.loc[df['Occupation']=='Doctor']
engineer=df.loc[df['Occupation']=='Engineer']
retired=df.loc[df['Occupation']=='Retired']
farmer=df.loc[df['Occupation']=='Farmer']
unemployed=df.loc[df['Occupation']=='Unemployed']
print("The number of doctor:\n",len(doctor))
print("The number of engineer:\n",len(engineer))
print("The number of retired:\n",len(retired))
print("The number of unemployed:\n",len(unemployed))

older_than_40=df.loc[df['Age']>=40]
print("The number of people who are older than 40 years:\n",len(older_than_40))
Genz=df.loc[df['Age']<=21]
print("The total number of GenZ:\n",len(Genz))

unique_occupation=df['Occupation'].unique()
print("Total unique occupations:\n",len(unique_occupation))
