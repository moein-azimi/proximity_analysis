import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import lifelines
from lifelines import KaplanMeierFitter


def check(x):
    if x == 'yes' :
        return 1
    elif x == 'no':
        return 0


df = pd.read_csv('file.csv')
df['dfs_event'] = df['dfs_event'].apply(check)
df.drop(columns=df.columns[0], axis=1, inplace=True)


#df = df.loc[(df['dfs_event'] == 'no')]

# Increase the size of the heatmap.
plt.figure(figsize=(16, 6))
# Store heatmap object in a variable to easily access it when you want to include more features (such as title).
# Set the range of values to be displayed on the colormap from -1 to 1, and set the annotation to True to display the correlation values on the heatmap.
heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
# Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);
plt.show()

'''

df_yes = df.loc[(df['dfs_event'] == 'yes')]
df_no = df.loc[(df['dfs_event'] == 'no')]

print(df_yes.describe())
ax = plt.subplot()
kmf = KaplanMeierFitter()
kmf.fit(durations=df_yes['dfs_months'], label='yes')
kmf.plot_survival_function(figsize=(8,5), ax=ax)
kmf.fit(durations=df_no['dfs_months'], label='no')
kmf.plot_survival_function(figsize=(8,5), ax=ax)
plt.title('Survival Function based on event')
plt.show()

'''


'''
df = pd.read_csv('E:/GE/neighbor/data/MSK_stage3_clinical_TMAmap_selected.csv')

df = df[['dfs_months'] + ['dfs_event']]
df = df.dropna()
print(df)


df['dfs_months'] = df['dfs_months'].apply(lambda x: int(x))


kmf = KaplanMeierFitter()
#kmf.fit(durations=df['dfs_months'], event_observed=df['dfs_event'])
kmf.fit(durations=df['dfs_months'])

kmf.survival_function_.plot(figsize=(8,5))
plt.title('Survival Curve estimated with Kaplan-Meier Fitter')
plt.show()

kmf.plot_survival_function(figsize=(8,5))
plt.title('Survival Curve estimated with Kaplan-Meier Fitter with confidence intervals')
plt.show()
'''