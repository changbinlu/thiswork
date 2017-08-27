import gensim
# Load Google's pre-trained Word2Vec model.
import pandas as pd
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)  
df = pd.read_csv('nature_result.txt')
f = open('4900.txt','w')
for index,row in df.iterrows():
    if df['word'][index] not in model.wv.vocab:
	continue
    temp = model.most_similar(df['word'][index])
    f.write('{},{},{},{},{},{},{},{},{},{},{}\n'.format(df['word'][0],df['freq'][0],temp[0][0].encode('ascii','ignore'),temp[1][0].encode('ascii','ignore'),temp[2][0].encode('ascii','ignore'),temp[3][0].encode('ascii','ignore'),temp[4][0].encode('ascii','ignore'),temp[5][0].encode('ascii','ignore'),temp[6][0].encode('ascii','ignore'),temp[7][0].encode('ascii','ignore'),temp[8][0].encode('ascii','ignore')))

f.close()
