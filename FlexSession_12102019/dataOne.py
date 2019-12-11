#%%
import pandas as pd
import os
#%%
dataFile = 'a:\\DataVizRepo\\FlexSession_12102019\\DataOne.csv'
#%%
def genderToInt(gender: str) -> int:
    if gender == "Male":
        return 0
    else:
        return 1
#%%
dataFilePD = pd.read_csv(dataFile)
#%%
#dataFileGender = genderToInt(dataFilePD["Gender"])
dataFileGender = dataFilePD["gender"].apply(genderToInt)
#%%
dataFilePD["Gender Numerical Value"] = dataFileGender

# %%
dataFilePD

# %%
