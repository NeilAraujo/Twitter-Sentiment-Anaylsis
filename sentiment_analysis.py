import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

vds=SentimentIntensityAnalyzer()

def sentiment_table(text):
	return vds.polarity_scores(text)


australia=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_data\\clean_australia.csv")
canada=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_data\\clean_canada.csv")
india=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_data\\clean_india.csv")
uk=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_data\\clean_uk.csv")
us=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_data\\clean_us.csv")


nan_value = float("NaN")
australia.replace("",nan_value,inplace=True)
australia.dropna(inplace=True)
canada.replace("",nan_value,inplace=True)
canada.dropna(inplace=True)
india.replace("",nan_value,inplace=True)
india.dropna(inplace=True)
uk.replace("",nan_value,inplace=True)
uk.dropna(inplace=True)
us.replace("",nan_value,inplace=True)
us.dropna(inplace=True)


australia=australia.text.apply(lambda x:sentiment_table(x))
canada=canada.text.apply(lambda x:sentiment_table(x))
india=india.text.apply(lambda x:sentiment_table(x))
uk=uk.text.apply(lambda x:sentiment_table(x))
us=us.text.apply(lambda x:sentiment_table(x))


australia.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_sentiment_values\sentiment_australia.csv",index=True)
canada.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_sentiment_values\sentiment_canada.csv",index=True)
india.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_sentiment_values\sentiment_india.csv",index=True)
uk.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_sentiment_values\sentiment_uk.csv",index=True)
us.to_csv(r"C:\Users\Neil Araujo\Documents\webmining\tweet_analysis\vader_sentiment_values\sentiment_us.csv",index=True)

