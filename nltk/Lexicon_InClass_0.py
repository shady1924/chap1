# Import pandas package to store and manipulate data
import pandas as pd

# Import csv package to convert pandas dataframe to csv file
import csv

# Import Counter package to do counting
from collections import Counter

# Import operator package to sort a dictoinary by its values
import operator

# Import NTLK package after the installation
from nltk import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

import nltk
nltk.download()

# ### **Lexicon-based Word Counting**
# We use [General Inquirer](http://www.wjh.harvard.edu/~inquirer/), a free dictionary, to analyze reveiw sentiment.

# **Import positive and negative words from General Inquirer Dictionary**
positive=[]
negative=[]
keys_to_ignore = ['Entry','Source','Defined']
with open('general_inquirer_dict.txt') as fin:
    reader = csv.DictReader(fin,delimiter='\t')
    for i,line in enumerate(reader):
        if line['Negativ']=='Negativ':
            if line['Entry'].find('#')==-1:
                negative.append(line['Entry'].lower())
            if line['Entry'].find('#')!=-1: #In General Inquirer, some words have multiple senses. Combine all tags for all senses.
                negative.append(line['Entry'].lower()[:line['Entry'].index('#')]) 
        if line['Positiv']=='Positiv':
            if line['Entry'].find('#')==-1:
                positive.append(line['Entry'].lower())
            if line['Entry'].find('#')!=-1: #In General Inquirer, some words have multiple senses. Combine all tags for all senses.
                positive.append(line['Entry'].lower()[:line['Entry'].index('#')])

fin.close()

# Store positive words and negative words from the dictionary in two lists
pvocabulary=sorted(list(set(positive))) 
nvocabulary=sorted(list(set(negative))) 
print(stopwords.words("english"))
review=pd.read_csv("demo_data_review_1k.csv")
print(review.columns.values)
# review=review[['review_id','business_id','text','stars','visitfuture','visits']]

