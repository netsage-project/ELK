import pandas as pd
import time
import numpy as np

df = pd.read_csv('/mnt/ssd/flowout1397.csv', names=['Flow_start','Flow_end','Time_Duration','Source_IP','Destination_IP','Source_port','Destination_port','Protocol','Flag','N1','N2','Input_packet','Input_Byte','N3','N4','N5','N6','Source_AS','Destination_AS'])
df['Flow_start'] = pd.to_datetime(df['Flow_start'],format='%Y-%m-%d %H:%M:%S')
df['Flow_end'] = pd.to_datetime(df['Flow_end'],format='%Y-%m-%d %H:%M:%S')
df['BPS'] = 0

partialDF = df[df['Flag']==".AP..."]

size = 0
for index, row in partialDF.iterrows():
    size =  row['Input_Byte']
    previous_index = index-1
    df.iat[previous_index,12] = df.iat[previous_index,12]+size
    

df = df[df['Flag']!=".AP..."]

df['BPS']=df['Input_Byte']/df['Time_Duration'].astype(int)
df['BPS'] = df['BPS'].astype(int)
df

df.to_csv("/home/aasingh/flowpro/processedflowout1397.csv")


