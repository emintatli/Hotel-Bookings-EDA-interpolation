import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("../input/hotel-booking-demand/hotel_bookings.csv")

df.head(5)

df.info()

df.isnull().values.any()
df2=df.select_dtypes(exclude='object')
df2.info()

df2.isnull().sum()

df_out=df2.copy()
def outlier(df,column):
    df_out=[]
    for each in column:   
     Q1=np.percentile(df[column],25)
     Q2=np.percentile(df[column],50)
     Q3=np.percentile(df[column],75)
     QQ=[Q1-1.5*(Q3-Q1),Q3+1.5*(Q3-Q1)]
     df_outliers=df[column][(df[column]>QQ[1]) | (df[column]<QQ[0])]
     df_outliers.dropna(axis=0,inplace=True)
     df_out.extend(df_outliers.index)
    df_count=Counter(df_out)
    return df_out
outlier(df_out,["children","adults","booking_changes","agent","company","days_in_waiting_list","adr","required_car_parking_spaces","total_of_special_requests"])


df2[df2["children"].isnull()]

df2[df2["adults"]==2].children.mean()

df2[(df2["adults"]==2) & (df2["children"].isnull())]=0

df2.loc[40667].children

df2[df2["adults"]==3].children.mean()

df2[(df2["adults"]==3) & (df2["children"].isnull())]=0

df2[df2["children"].isnull()]

df2.corr() # corelation

f,ax=plt.subplots(figsize=(13,13))
sns.heatmap(df2.corr(),annot=True,linewidths=.5,fmt=".1f",ax=ax)
plt.show()

df2[df2["agent"].isnull()]
df2.drop(df2[(df2["agent"].isnull()) & (df2["company"].isnull())].index,axis=0,inplace=True)

df2[df2["agent"].isnull()]

df_ac=df2[(df2["agent"].isnull()==False) & (df2["company"].isnull()==False)][["agent","company"]].reset_index(drop=True)

df_ac["agent"].sum()/df_ac["company"].sum()
#0.7730   company*0.773=agent

def agent_value(value):
    return value*0.773
def company_value(value):
    return value/0.773
df_tofix=df2[(df2["agent"].isnull())].reset_index(drop=True)
df_tofix["agent"]=df_tofix["company"].apply(agent_value)
df_tofix=df2[(df2["company"].isnull())].reset_index(drop=True)
df_tofix["company"]=df_tofix["agent"].apply(company_value)
df_tofix


df_tofix.isnull().sum()

