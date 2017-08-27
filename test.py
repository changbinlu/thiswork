from __future__ import unicode_literals, print_function
import MySQLdb as sql
import pandas as pd
import time
import random

import os

from zhihu_oauth import ZhihuClient


TOKEN_FILE = 'token.pkl'


client = ZhihuClient()

if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
else:
    client.login_in_terminal()
    client.save_token(TOKEN_FILE)



db_connection = sql.connect(host='localhost', db='zhihu', user='root', passwd='123', charset = 'utf8')
cur=db_connection.cursor() 
sql = "insert into final values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

df = pd.read_sql('SELECT distinct * FROM user', con=db_connection)



for i in range(400009,700000):
    randomTime = random.uniform(1,2) 
    time.sleep(randomTime) 
    url = 'http://www.zhihu.com/people/' + df['user_token'][i]
    author = client.from_url(url)
    try:
      topic = author.following_topics
    except:
      pass
    j = 0
    for t in topic:
        j = j + 1
        if(j == 1):
            df['topic1'][i] = t.name
        elif(j == 2):
            df['topic2'][i] = t.name
        elif(j == 3):
            df['topic3'][i] = t.name   
        elif(j == 4):
            df['topic4'][i] = t.name
        elif(j == 5):
            df['topic5'][i] = t.name
            break
    
    cur.execute(sql,(df['id'][i],df['user_token'][i],df['location'][i],df['business'][i],df['sex'][i],
                    df['employment'][i],df['education'][i],df['username'][i],df['url'][i],df['agrees'][i],
                    df['thanks'][i],df['asks'][0],df['answers'][i],df['posts'][i],df['followees'][i],
                    df['followers'][i],df['topic1'][i],df['topic2'][i],df['topic3'][i],df['topic4'][i],
                    df['topic5'][i],df['hashId'][i]))
    db_connection.commit()
    print(i)
    print(df['topic1'][i] )
    

cur.close()
db_connection.commit()
db_connection.close()

        
