# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:02:40 2019

@author: hp
"""
import numpy as np #
import matplotlib.pyplot as plt # Plotting
import matplotlib.colors as colors # Coloring
import seaborn as sns # Statistical visualization
import pandas as pd
df=pd.read_excel('volcano_data.xlsx')
test=[]
for i in df.index.values:
     row_data=df.ix[i,['log2FoldChange','padj']].to_dict()
     test.append(row_data)
#print("最终获取到的数据是：{0}".format(test))
data1 = pd.DataFrame(test)
# In[*]
result = data1
result.columns = ['fold','pvalue']
result['log(pvalue)'] = -np.log2(result['pvalue'])
# In[*]
result['sig'] = 'normal'
result['size']  =np.abs(result['fold'])/10
result.loc[(result.fold> 1 )&(result.pvalue < 0.05),'sig'] = 'up'
result.loc[(result.fold< -1 )&(result.pvalue < 0.05),'sig'] = 'down'
# In[*]
ax = sns.scatterplot(x="fold", y="log(pvalue)",
                      hue='sig',
                      hue_order = ('down','normal','up'),
                      palette=("#377EB8","green","#E41A1C"),
                      data=result)
ax.set_ylabel('-log2(pvalue)',fontweight='bold')
ax.set_xlabel('FoldChange',fontweight='bold')
