import sqlite3
from sqlite3 import Error
import stream as st
from time import strftime


stream = st.create_stream()
tweets, dt, future = st.get_stream(stream)


conn = sqlite3.connect("assign2.db")
db = conn.cursor()
db.execute('drop table if exists HASHTAGS;')
db.execute('create table HASHTAGS (tag_ID integer primary key autoincrement,hashtag text);')
conn.commit()


for tweet in tweets:
        hashtags = tweet['entities']['hashtags']
        for hashtag in hashtags:
            # print "%s" % (hashtag['text'])
            db.execute('INSERT INTO HASHTAGS (hashtag) VALUES (?);', [hashtag['text']])
            conn.commit()

cur = db.execute('select hashtag, count(*) as count from HASHTAGS group by hashtag order by count desc limit 10;')
top10 = cur.fetchall()

fp = open('assign2-report.txt', 'w')

print('{}\t{}'.format(dt,future))
fp.write('{}\t{}\n'.format(dt,future))
for tag in top10:
    print(tag[0] + '\t{}'.format(tag[1]))
    fp.write(tag[0] + '\t{}\n'.format(tag[1]))

conn.close()