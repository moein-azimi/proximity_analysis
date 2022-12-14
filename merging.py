import pandas as pd
import os
import numpy as np
import math

path = 'E:/GE/neighbor2/data2/'

x = [item for item in os.listdir(path)] 


#MSK2020_1-yes-76-female-19    otherim+cancer   thelper+cancer   thelperReg+cancer  tkiller+cancer  


df_cols = ['patient', 'dfs_event' , 'age', 'gender', 'dfs_months', 'otherim+cancer', 'thelper+cancer', 'thelperReg+cancer', 'tkiller+cancer']
new_df = pd.DataFrame(columns=df_cols)




def check(x):
    if x >= 0 :
        return x
    else:
        return 0



for i in range(len(x)):
    df = pd.read_csv(path+x[i])
    df['otherim+cancer'] = df['otherim+cancer'].apply(check)
    df['thelper+cancer'] = df['thelper+cancer'].apply(check)
    df['thelperReg+cancer'] = df['thelperReg+cancer'].apply(check)
    df['tkiller+cancer'] = df['tkiller+cancer'].apply(check)
    new_df.loc[len(new_df.index)] = [x[i].split('-')[0],x[i].split('-')[1],int(x[i].split('-')[2]),x[i].split('-')[3],int(x[i].split('-')[4].replace('.csv','')),df['otherim+cancer'].mean(),df['thelper+cancer'].mean(),df['thelperReg+cancer'].mean(), df['tkiller+cancer'].mean()]


new_df.to_csv('file.csv')