import time
from progressbar import ProgressBar
import pandas as pd
pbar = ProgressBar()
df = pd.read_csv('4900.txt', error_bad_lines=False)
df1 = pd.read_csv('4900.txt', error_bad_lines=False)
for index,rows in pbar(df.iterrows()):
    bag = [df['s0'][index],df['s1'][index],df['s2'][index],df['s3'][index],df['s4'][index],df['s5'][index],df['s6'][index],df['s7'][index],df['s8'][index],df['s9'][index]]
    for index1,rows1 in df1.iterrows():
        if df1['word'][index1] in bag:
            df['freq'][index] = int(df['freq'][index]) + int(df1['freq'][index1])
            df.drop(df.index[index1])


df.to_csv('GoogleModelMergeResult1.csv')
