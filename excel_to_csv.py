import pandas as pd
data_xls = pd.read_excel('All_Training_Data.xlsx','Sheet 1')
data_xls.to_csv('All_Training_Data.csv', encoding='utf-8',index=False)
