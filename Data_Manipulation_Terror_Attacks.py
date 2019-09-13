import pandas as pd
import numpy as np
missing_value=["Na","NAN","n/a","n.a.","na","NaN","nan"]
Df=pd.read_csv(r"C:\Users\Noel\.anaconda\DataSci\Assignments\terror.csv",sep=",",header=0,encoding='latin', na_values=missing_value, low_memory=False)
check1=Df.country_txt=="India"
check2=(Df.country_txt=="India")&(Df.nkill<=3)
cols = ["attacktype1","attacktype2","attacktype3"]

#First solution
Df['Total_attack'] = Df.loc[check1,cols].sum(axis=1).fillna(0)
Total_attack = Df['Total_attack'].sum()
print (Total_attack)

#Second Solution
Df['Total_attack'] = Df.loc[check2,cols].sum(axis=1).fillna(0)
Total_attack = Df['Total_attack'].sum()
print (Total_attack)

#Third solution
cols2=["summary","city"]
Sum_city= Df.loc[check1,cols2]
print (Sum_city)

#Fourth solution
disp=Df[check1].groupby("city").agg({'nkill':np.sum}).sort_values("nkill",ascending=False).head(5)
print(disp)

#Fifth Solution
Df["nsum"]=Df[["nkill","nwound"]].sum(axis=1)

nsum=Df[check1].groupby("city").agg({'nsum':np.sum}).sort_values("nsum",ascending=False).head(5)
print(nsum)

#Sixth Solution
check3=(Df.success==1)&(Df.suicide==1)&(check1)
Df['Total_attack'] = Df.loc[check3,cols].sum(axis=1).fillna(0)
Total_attack = Df['Total_attack'].sum()
print(Total_attack)

#Seventh Solution   
Label=Df["nkill"].apply(lambda x:"Severe"if x>5 else"Minor")
print(Label)

#Eighth Solution
def succ_suicidal(x, y):
   if x==y:
    return 'Both succesful and suicidal'
   else :
    return 'No match'
label2=Df[['success','suicide']].apply(lambda x:succ_suicidal("success","suicide"), axis=1)
print(label2)

#Ninth Solution
def create_label(x):
    
 if x=="Afghanistan":
     return "Afg-Pak_India"
 if x=="Pakistan":
     return "Afg-Pak_India"
 if x=="India":
     return "Afg-Pak_India"
             
 else:
  return "ROW"
  
Df["Local"]=Df["country_txt"].apply(create_label)
print(Df["Local"])

#Tenth Solution
n_incidents=Df["Local"].value_counts()
print(n_incidents)

#Eleventh Solution

print(Df.groupby("Local", as_index=False).agg({"nkill":np.mean,"suicide":np.sum}).rename(columns={'nkill':'average_kills','suicide':'no. of suicides'}))
