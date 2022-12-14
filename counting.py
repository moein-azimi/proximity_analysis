import os
import pandas as pd
import numpy as np


def counting(str1, str2, df1, df2, path):
    df1[f'{str1}+{str2}'] = -1
    for index1, row1 in df1.iterrows():
        count = 0
        for index2, row2 in df2.iterrows():
            m = np.sqrt((row1['CellCentroid.X']-row2['CellCentroid.X'])**2+(row1['CellCentroid.Y']-row2['CellCentroid.Y'])**2)
            if m < 120 and m != 0:
                count = count + 1 
            #print(row1['ID'],row2['ID'],row1['CellCentroid.X'],row2['CellCentroid.X'],row1['CellCentroid.Y'],row2['CellCentroid.Y'])
        print(row1['ID'], count)
        df1.at[index1, f'{str1}+{str2}'] = count
        #A.append(count)
    return df1.to_csv(path)
        

def read_files(path):
    x = [item for item in os.listdir(path) if item.endswith('.csv')]
    return x

path = 'E:/GE/neighbor2/data/'


A = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
B = []
C = []

for i in range(len(A)):
    B.append(path+A[i])
    C.append(path+A[i]+'/SS/')

#file names
Cancer = read_files(C[0])


for i in range(1,len(A)):
    for j in range(len(Cancer)):
        try:
            df1 = pd.read_csv(C[0]+Cancer[j])
            df2 = pd.read_csv(C[i]+Cancer[j])
            print(Cancer[j], '  starting...')
            counting(A[i], A[0], df1, df2, C[0]+Cancer[j])
        except:
            print(A[i], A[0], 'not exist...',Cancer[j])
            df1[f'{A[i]}+{A[0]}'] = -1
            df1.to_csv(C[0]+Cancer[j])
            pass
