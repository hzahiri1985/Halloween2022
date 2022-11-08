import datetime
import pandas as pd 
import glob
from datetime import datetime as dt
import matplotlib.pyplot as plt 
#import all the files into datafarme 
df1 = pd.read_csv("halloween2019a.csv", sep=',')
print(df1.head())
df2 = pd.read_csv("halloween2019a.csv", sep=',')
print(df2.head())
df3 = pd.read_csv("halloween2019a.csv", sep=',')
print(df3.head())

#drop the column with a lot of NA (MiddleName

df1 = df1.drop(['MiddleName'], axis=1)
df2 = df2.drop(['MiddleName'], axis=1)
df3 = df3.drop(['MiddleName'], axis=1)

#drop na values 

#df1
df1 = df1.dropna()
nulls1 = df1.isna().sum()
print(nulls1)

#df2
df2 = df2.dropna()
nulls2 = df2.isna().sum()
print(nulls2)
#df3
df3 = df3.dropna()
nulls3 = df3.isna().sum()
print(nulls3)
##########################################
#parse date for dataset#1
def parse_date(df1, cols):
    for col in cols:
        df1[col] = df1[col].apply(lambda x: pd.to_datetime(x).strftime("%Y"))
        df1[col] = pd.to_datetime(df1[col], format = "%Y")
    return df1

df1 = parse_date(df1, ["DOB", "DOD"])
print(df1)
#parse date for dataset#2

df2 = parse_date(df2, ["DOB", "DOD"])
print(df2)

#parse date for dataset#2
df3 = parse_date(df3, ["DOB", "DOD"])
print(df3)


###########################################################################################
#combine all files 
list = ['FirstName', 'LastName', 'DOB', 'DOD']
df4 = df1.merge(df2,
                   on = list,
                   how = 'outer')                   
print(df4)

df_master = df4.merge(df3,
                        on = list,
                        how = 'outer')
print(df_master)
##############
#droping date and month for DOB & DOD
df_master['DOB'] = df_master['DOB'].dt.strftime('%Y')
df_master['DOD'] = df_master['DOD'].dt.strftime('%Y')
print(df_master)


df_master.groupby(pd.Grouper(key='DOB', freq='1Y')).sum()
# convert DOB abd DOD to int 

df_master = pd.DataFrame(df_master)
df_master = df_master.astype({"DOB":"int","DOD":"int"})

df_master['life span'] = df_master['DOD'] - df_master['DOB']
print(df_master)


df_master.hist(column='life span')
plt.savefig('price_histogram.png')












