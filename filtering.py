import os
import pandas as pd
import numpy as np

'''
General immune cell are defined as: immune$CD3CD20 == “CD3+”

Some of the subtypes within immune cells:

T-helper cells: immune$CD4CD8 == “CD4+” & immune$CD3CD20 == “CD3+”
T-killer cells: immune$CD4CD8 == “CD8+” & immune$CD3CD20 == “CD3+”

Regulatory T cells: immune$CD4CD8 == “CD4+” & immune$CD3CD20 == “CD3+” & immune$FOXP3 == “FOXP3+” & immune$PD1 == "Neg"

* For T-reg cells, we included PD1 negative to be consistent with Xanthi’s paper
'''

pathcancer = 'E:/GE/neighbor2/data/cancer/'
isExist = os.path.exists(pathcancer)
if not isExist:
   os.makedirs(pathcancer)

paththelper = 'E:/GE/neighbor2/data/thelper/'
isExist = os.path.exists(paththelper)
if not isExist:
   os.makedirs(paththelper)
   
pathtkiller = 'E:/GE/neighbor2/data/tkiller/'
isExist = os.path.exists(pathtkiller)
if not isExist:
   os.makedirs(pathtkiller)
   
paththelperReg = 'E:/GE/neighbor2/data/thelperReg/'
isExist = os.path.exists(paththelperReg)
if not isExist:
   os.makedirs(paththelperReg)
   
pathotherim = 'E:/GE/neighbor2/data/otherim/'
isExist = os.path.exists(pathotherim)
if not isExist:
   os.makedirs(pathotherim)

pathstroma = 'E:/GE/neighbor2/data/stroma/'
isExist = os.path.exists(pathstroma)
if not isExist:
   os.makedirs(pathstroma)
   
df = pd.read_csv('E:/GE/neighbor/data4/Modified_ ColonRO1_2020_MSK_stage3_immune_processed.csv')
cols = list(df.columns.values)
df1 = df[cols[2:8]+cols[14:-1]+[cols[-1]]]
#df = df.loc[df['Epithelium.Stroma'] == 2]
df2 = df1.loc[(df1['Epithelium.Stroma'] == 1) & (df1['CD3CD20'] != 'CD3+')]
df2.to_csv(pathcancer+'cancer.csv')

df3 = df1.loc[(df1['CD3CD20'] == 'CD3+') & (df1['CD4CD8'] == 'CD4+')]
df3.to_csv(paththelper+'thelper.csv')

df4 = df1.loc[(df1['CD3CD20'] == 'CD3+') & (df1['CD4CD8'] == 'CD8+')]
df4.to_csv(pathtkiller+'tkiller.csv')

df5 = df1.loc[(df1['CD3CD20'] == 'CD3+') & (df1['CD4CD8'] == 'CD4+') & (df1['FOXP3'] == 'FOXP3+') & (df1['PD1'] == 'Neg') ]
df5.to_csv(paththelperReg+'thelperReg.csv')

df6 = df1.loc[(df1['CD3CD20'] == 'CD3+') & (df1['CD4CD8'] != 'CD4+') & (df1['CD4CD8'] != 'CD8+')]
df6.to_csv(pathotherim+'otherim.csv')

df7 = df1.loc[(df1['Epithelium.Stroma'] == 2) & (df1['CD3CD20'] != 'CD3+')]
df7.to_csv(pathstroma+'stroma.csv')

'''
df = pd.read_csv('ColonRO1_2020_MSK_stage3_immune_processed.csv')
cols = list(df.columns.values)
df1 = df[cols[2:7]+cols[13:-1]+[cols[-1]]]
df2 = df1.loc[df1['Epithelium.Stroma'] == 2]
df2.to_csv('stroma.csv')
'''