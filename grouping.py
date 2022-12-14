import numpy as np
import pandas as pd
import os 

thedir = 'E:/GE/neighbor2/data/'
x = [name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name))]


for i in range(len(x)):
    path = thedir+x[i]+'/'+'SS/'
    isExist = os.path.exists(path)
    if not isExist:
       os.makedirs(path)
    df = pd.read_csv(thedir+x[i]+'/'+x[i]+'.csv')
    print(thedir+x[i]+'/'+x[i]+'.csv')
    for j, k in df.groupby('SS'):
        p = os.path.join(path, '{}.csv'.format(j.upper()))
        k.to_csv(p,index=False)
