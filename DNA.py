
# coding: utf-8

# In[191]:


import os 
import pandas as pd 
os.chdir("C:/Users/Dell/Documents/Documenntnnttnn/TGB- Assignment")


# In[192]:


os.getcwd()


# In[193]:


# Read the data into a pandas DataFrame and do some EDA
data = pd.read_csv('Problem.txt', sep='\t', dtype={'Annotation':'str', 'Chr':'object', 'Position':'int', 'Genotypes':'str'}, comment='#')


# In[194]:


data


# In[195]:


data.head()


# In[196]:


df= (pd.DataFrame(data))


# In[197]:


df


# In[198]:


df.head(25)


# In[199]:


df.isnull().any()


# In[200]:


df.nunique()


# In[201]:


# How many chromosomes am I missing by not 
# having a Y chromosome?
Y_chromosome = df[df.Chr == 'Y']


# In[202]:


Y_chromosome


# In[203]:


len(Y_chromosome)


# In[204]:


#I converted the letter chromosomes to numbers, cast them to ints, and created a dictionary to translate them back later so that I could better manipulate the data.
df['Chr'].unique()


# In[205]:


import re
df['Chr'] = df['Chr'].apply(lambda x: 
  re.sub(r'X', r'23', x))
df['Chr'] = df['Chr'].apply(lambda x: 
  re.sub(r'MT', r'24', x))


# In[206]:


#df['Chr'] = df['Chr'].apply(lambda x: 
  #int(x))
Chr_dict = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 
           6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 
           11:'11', 12:'12', 13:'13', 14:'14', 
           15:'15', 16:'16', 17:'17', 18:'18', 
           19:'19', 20:'20', 21:'21', 22:'22', 
           23:'X', 24:'MT'}


# In[207]:


print(Chr_dict)
display(df.info())


# In[208]:


Genotypes_na = df[df.Genotypes == '--']
len(Genotypes_na)


# In[209]:


df[df.Chr == 1].info()


# In[210]:


#df.rename({' Annotation': 'Annotation'}, axis='columns', inplace=True)
df.rename(columns={c:c.lower() for c in df.columns})


# In[211]:


# We can do this manually with a for loop . . .
x = []
y = []
for k in Chr_dict:
    x.append(k)
    y.append(len(df[df.Chr == k]))
Annotation_per_Chr = dict(zip(x,y)) 


# In[212]:


Annotation_per_Chr


# In[213]:


# . . . but pandas makes it a lot easier!
Annotation_per_Chr_series = df.groupby('Chr')['Annotation'].count()
#Annotation_per_Che_series.columns = ['Chr', 'count']


# In[214]:


Annotation_per_Chr_series


# In[215]:


Annotation_per_Chr_series.columns = ['Chr', 'count']


# In[216]:


Annotation_per_Chr_series.columns


# In[217]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
Annotation_per_Chr_series.plot.barh(figsize=(16,9), fontsize=15)
plt.show()


# In[221]:


snp_df = pd.read_csv('Problem II - transform.txt')
snp_df.head()


# In[238]:


#new_cols = ['Annotations', 'Position', 'Genotype']
#new_df = snp_df.merge(df, how='inner', on=['annotations', 'genotypes']) 


# In[232]:


#ew_cols 


# In[230]:


#new_cols

