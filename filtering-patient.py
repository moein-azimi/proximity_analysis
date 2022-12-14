import os
import pandas as pd
import numpy as np


path = 'E:/GE/neighbor2/data/cancer/SS/'
path2 = 'E:/GE/neighbor2/data2/'

os.makedirs(path2)

x = [item for item in os.listdir(path) if item.endswith('.csv')] 


df = pd.read_csv('E:/GE/neighbor/data/MSK_stage3_clinical_TMAmap_selected.csv')

def filtering(df):
    df_new = df[['SS']+['ID']+['CellCentroid.X']+['CellCentroid.Y']+['Epithelium.Stroma']+['otherim+cancer']+['thelper+cancer']+['thelperReg+cancer']+['tkiller+cancer']]
    return df_new


for index, row in df.iterrows():
    for i in range(len(x)):
        try:
            if row['SS'] == x[i].replace('.csv',''):
                #print(row['SS'], x[i])
                df1 = pd.read_csv(path+x[i])
                df2 = filtering(df1)
                str0 = row['Patient']
                str1 = row['dfs_event']
                str2 = row['age']
                str3 = row['sex']
                str4 = row['dfs_months']
                if os.path.exists(path2+str(str0)+'-'+str(str1)+'-'+str(str2)+'-'+str(str3)+'-'+str(str4)+'.csv'):
                    df_new2 = pd.read_csv(path2+str(str0)+'-'+str(str1)+'-'+str(str2)+'-'+str(str3)+'-'+str(str4)+'.csv')
                    df_merge = pd.concat([df_new2,df2])
                    print('found new slide ', row['Patient'], row['SS'])
                    df_merge.to_csv(path2+str(str0)+'-'+str(str1)+'-'+str(str2)+'-'+str(str3)+'-'+str(str4)+'.csv')
                else:
                    print('first slide ', row['Patient'], row['SS'])
                    df2.to_csv(path2+str(str0)+'-'+str(str1)+'-'+str(str2)+'-'+str(str3)+'-'+str(str4)+'.csv')
                    
        except:
            pass
            print('not found', x[i].replace('.csv',''))
    
    