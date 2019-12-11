#%%
import pandas as pd
#%%
import os
#%%
#dataFile = os.path.join(os.getcwd(), 'FlexSession_12102019/dataSet.csv')
dataFile = 'a:\\DataVizRepo\\FlexSession_12102019\\dataSet.csv'
#%%
dataFilePD = pd.read_csv(dataFile)

# %%
dataFilePD.head(100)


# %%
dataFilePD.describe()

# %%
dataFilePD["Amount"].head(100)

# %%
dataFilePD["Amount"].describe()

# %%
dataFilePD[["Amount","Gender"]].head()

# %%
dataFilePD["Amount"].mean()

# %%
dataFilePD["Amount"].sum()

# %%
dataFilePD["Gender"].unique()

# %%
dataFilePD["Gender"].value_counts()

# %%
thousandsOfDollars = dataFilePD["Amount"]/1000
dataFilePD["Thousands Of Dollars"] = thousandsOfDollars
dataFilePD.head()


# %%
