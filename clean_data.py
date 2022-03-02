import pandas as pd
import preprocessor as p
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def clean_text(text):
    text=p.clean(text)
    return text


australia=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\big_dataset\\australia.csv")
canada=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\big_dataset\\canada.csv")
india=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\big_dataset\\india.csv")
uk=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\big_dataset\\uk.csv")
us=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\big_dataset\\us.csv")

#forming a separate feature for cleaned tweets
#for i,v in enumerate(australia.text):
#    australia.loc[v:'text'] = p.clean(i)

clean_australia=pd.DataFrame(australia.text)
clean_canada=pd.DataFrame(canada.text)
clean_india=pd.DataFrame(india.text)
clean_uk=pd.DataFrame(uk.text)
clean_us=pd.DataFrame(us.text)

clean_australia=clean_australia.text.apply(lambda x:clean_text(x))
print("aussie done")
clean_canada=clean_canada.text.apply(lambda x:clean_text(x))
print("canada done")
clean_india=clean_india.text.apply(lambda x:clean_text(x))
print("india done")
clean_uk=clean_uk.text.apply(lambda x:clean_text(x))
print("uk done")
clean_us=clean_us.text.apply(lambda x:clean_text(x))
print("us done")

clean_australia.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_data\clean_australia.csv",index=True)
clean_canada.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_data\clean_canada.csv",index=True)
clean_india.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_data\clean_india.csv",index=True)
clean_uk.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_data\clean_uk.csv",index=True)
clean_us.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_data\clean_us.csv",index=True)

print("finally done")

