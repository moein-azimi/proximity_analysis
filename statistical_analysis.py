import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

path = 'E:/GE/neighbor2/data/cancer/SS/'

x = [item for item in os.listdir(path) if item.endswith('.csv')] 



def Average(lst):
    return sum(lst) / len(lst)
def std(lst):
    return np.array(lst).std()

    

Yes = []
Avgyes = []
Nameyes = []
for i in range(len(xyes)):
    df = pd.read_csv(pathyes+xyes[i])
    list1 = [item for item in df['0'].values.tolist()]
    Avgyes.append(list1)
    Nameyes.append(xyes[i].replace('.csv','').replace('MSK2020_',''))
    for k in range(len(list1)):
        Yes.append(list1[k])

print(len(Avgyes))

plt.boxplot(Avgyes, labels=Nameyes)
plt.xlabel("Patients - Yes")
plt.ylabel("The number of neighbor cells")
plt.xticks(rotation=45)
plt.title("tkiller+cancer")
plt.show()

    
''' 
No = []
Avgno = []
Nameno =[] 
for i in range(len(xno)):
    df = pd.read_csv(pathno+xno[i])
    list1 = [item for item in df['0'].values.tolist()]
    Avgno.append(Average(list1))
    Nameno.append(xno[i].replace('.csv','').replace('MSK2020_',''))
    for k in range(len(list1)):
        No.append(list1[k])
            
            
import numpy as np
import matplotlib.pyplot as plt


# getting data of the histogram
count, bins_count = np.histogram(Yes, bins=40)
count2, bins_count2 = np.histogram(No, bins=40)
  
pdf = count / sum(count)
pdf2 = count2 / sum(count2)
  
cdf = np.cumsum(pdf)
cdf2 = np.cumsum(pdf2)
  
# plotting PDF and CDF
plt.plot(bins_count[1:], cdf, color="red", label="Yes")
plt.plot(bins_count[1:], cdf2, label="No")
plt.legend()
plt.savefig('tkiller+cancer.png')

from scipy.stats import kstest, ttest_ind


print(kstest(Yes, No))
print(ttest_ind(Yes, No))


import numpy as np
import matplotlib.pyplot as plt
 

fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(Nameyes, Avgyes, color ='maroon',
        width = 0.4)
 
plt.xlabel("Patients - Yes")
plt.ylabel("Average number of neighbor cells")
plt.xticks(rotation=45)
plt.title("tkiller+cancer")
plt.show()

print(Average(Avgyes))
print(Average(Avgno))


print(std(Avgyes))
print(std(Avgno))



import numpy as np
import matplotlib.pyplot as plt
 

fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(Nameno, Avgno, color ='maroon',
        width = 0.2)
 
plt.xlabel("Patients - No")
plt.xticks(rotation=88)
plt.ylabel("Average number of neighbor cells")
plt.title("tkiller+cancer")
plt.show()

# plotting PDF and CDF
plt.hist(Yes, bins=20)
_ = plt.xlabel("Yes")
_ = plt.ylabel("nums")

plt.show()

# plotting PDF and CDF
plt.hist(No, bins=20)
_ = plt.xlabel("No")
_ = plt.ylabel("nums")

plt.show()
'''