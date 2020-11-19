import string
from collections import Counter
import pandas

import matplotlib.pyplot as plt

# reading text file
#text = open("read.txt", encoding="utf-8").read()

df = pandas.read_csv('test1.csv')

df['Text'] = df['Text'].str.lower()
df['Text'] = df['Text'].to_string()
#df['cleaned'] = df['Text'].apply(lambda x: x.replace(c,'') for c in string.punctuation)
#df['cleaned'] = df['Text'].apply(lambda x:''.join([i for i in x 
 #                                                 if i not in string.punctuation]))
for index, row in df.iterrows():
    print(row)
    result = row.str.find('\n') 
    print ("Substring "'\n'" found at index:", result )
    df["Text"] = df["Text"].str.replace("b'#anonymous_confession_", "")

print(df.head(4))
#text=""
#text=df
# converting to lowercase
#df['cleaned'] = df['Text'].apply(lambda x: x.replace(c,'') for c in string.punctuation)
#df['cleaned'] = df['Text'].apply(lambda x:''.join([i for i in x 
 #                                                 if i not in string.punctuation]))
##def remove_punctuation(s):
 #   s = ''.join([i for i in s if i not in frozenset(string.punctuation)])
  #  return s

#df['cleaned'] = df['Text'].apply(remove_punctuation)
#tokenized_words = df['cleaned']
#print(df.head(4))
#stop_words = ["saya "," saya "," saya sendiri "," kita "," kita "," milik kita "," diri kita sendiri "," anda "," anda "," milik anda "," diri anda ",
 #             "dirimu sendiri", "dirinya", "dia", "miliknya", "dirinya", "itu", "itu", "itu sendiri",
 #             "mereka", "mereka", "mereka", "mereka", "mereka sendiri", "apa", "yang", "siapa", "siapa", "ini", "itu", "ini",
  #            "They", "am", "is", "are", "was", "were", "be", "be", "being", "have", "has", "had", "έχοντας "," lakukan ",
   #           "adakah", "lakukan", "melakukan", "a", "an", "the", "dan", "but", "if", "atau", "kerana", "as", "sampai "," sementara ",
    #          "of", "at", "by", "for", "with", "about", "melawan", "between", "into", "through", "during", "before",
     #         "selepas", "di atas", "di bawah", "ke", "dari", "atas", "bawah", "dalam", "keluar", "on", "mati", "lebih", "di bawah "," sekali lagi ",
      #        "lebih jauh", "kemudian", "sekali", "di sini", "ada", "kapan", "di mana", "mengapa", "bagaimana", "semua", "mana-mana", "keduanya", "masing-masing ",
       #       "sedikit", "lebih", "kebanyakan", "lain", "beberapa", "seperti", "tidak", "atau", "tidak", "hanya", "sendiri", "sama", "jadi "," daripada ",
        #      "too", "sangat", "s", "t", "boleh", "akan", "just", "don", "harus", "sekarang"]

# Removing stop words from the tokenized words list
#final_words = []
#for word in tokenized_words:
 #   if word not in stop_words:
  #      final_words.append(word)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

