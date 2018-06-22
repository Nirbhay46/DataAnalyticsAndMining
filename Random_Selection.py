import numpy as np
import pandas as pd
s=np.arange(10000)
print(s)
indices = np.random.shuffle(s)
print(indices)
final = np.array(s[:300])
print(final)
f=[]
for i in final:
    f.append(i)
df = pd.read_csv("All_Training_Data.csv")
training_df = df.loc[f]
print(training_df)
training_df.to_csv("Training_set.csv",encoding='utf-8',index=False)