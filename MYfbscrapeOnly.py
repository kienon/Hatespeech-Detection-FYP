import csv
import sys
#import pandas as pd

from facebook_scraper import get_posts
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
with open('UMSeHate.csv', 'a', newline='') as f:
   # expData= pd.DataFrame(post, fieldnames = ['PostID','Times','Texts'])
  #  thewriter = csv.DictWriter(f, fieldnames)
    
  #  thewriter.writeheader()
   # for i in range(1,100):
        try:
            for post in get_posts('386911624740468', pages=10):
                #print(post['post_id'])
                #print(post['time'])
                print(post['text'].translate(non_bmp_map))
                #print(post['likes'])
                #print(post['comments'])
               # thewriter.writerow([post['postID':'post_id'].encode('utf-8')])
        except AttributeError:
            print("No more posts to get")
            post.to_csv('UMShate.csv')
 
    
"""   

import csv
import sys

from facebook_scraper import get_posts
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
csvFile = open('UMSehate.csv', 'a')
csvWriter = csv.writer(csvFile)

try:
    for post in get_posts('386911624740468', pages=100):

        print(post['text'].translate(non_bmp_map)) 
        #csvWriter.writerow([post['text'].encode('utf-8')])

except AttributeError:
    print("No more posts to get")
    post.to_csv('UMSehate.csv')
"""

    