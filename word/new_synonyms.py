import pandas as pd
from PyDictionary import PyDictionary
dictionary=PyDictionary()
df = pd.read_csv('nature_result.txt')
f = open('nature_synonyms.txt','w')
for index,row in df.iterrows(): 
    print(index)
    temp = dictionary.synonym(df['word'][index])
    if len(temp) == 1:
            f.write('{},{},{}\n'.format(df['word'][index],df['freq'][index],temp[0].encode('ascii','ignore')))
    elif len(temp) == 2:
            f.write('{},{},{},{}\n'.format(df['word'][index],df['freq'][index],temp[0].encode('ascii','ignore'),temp[1].encode('ascii','ignore')))
    elif len(temp) == 3:
            f.write('{},{},{},{},{}\n'.format(df['word'][index],df['freq'][index],temp[0].encode('ascii','ignore'),temp[1].encode('ascii','ignore'),temp[2].encode('ascii','ignore')))
    elif len(temp) == 4:
            f.write('{},{},{},{},{},{}\n'.format(df['word'][index],df['freq'][index],temp[0].encode('ascii','ignore'),temp[1].encode('ascii','ignore'),temp[2].encode('ascii','ignore'),temp[3].encode('ascii','ignore')))
    elif len(temp) == 5:
            f.write('{},{},{},{},{},{},{}\n'.format(df['word'][index],df['freq'][index],temp[0].encode('ascii','ignore'),temp[1].encode('ascii','ignore'),temp[2].encode('ascii','ignore'),temp[3].encode('ascii','ignore'),temp[4].encode('ascii','ignore')))

f.close()
