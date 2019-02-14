
#generate a set of rules to filter results from my html analysis

# blacklist = all single letter "words"
#             top 100 from words dataframe
#             http, https, www, com, net, ahref, div etc.

# whitelist = start with manual selection of words
#             three word phrases
#             pear, banana, apple, daily, friend

import pandas as pd
import string
array = []
array1 = (string.ascii_lowercase)
for i in array1:
    array.append(i)

whitelist = ["include","your","white","list","items","here"]
#goal would be to apply blacklist filters, then expand the whitelist from surrounding words in 3 word results

blacklist = ["div","style","fonts","href","href","class","font", "color", "seo"]
#at this point array is an array of all single letters
blacklist = array+blacklist

df = pd.read_csv("html_3.csv",encoding = "UTF-8")
df.head()

length = len(whitelist)-1
array = []
for i in range(0,length):
    array.append(df[df['Unnamed: 0'].str.contains(" "+whitelist[i]+" ")])
    array.append(df[df['Unnamed: 0'].str.contains(whitelist[i]+" ")])
    array.append(df[df['Unnamed: 0'].str.contains(" "+whitelist[i])])

array = pd.concat(array)

# filt = array[array.phrase3 >100]
# filt.to_csv('over100countwhitelist.csv')
