import pandas as pd
import matplotlib.pyplot as plt

vader_australia=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_australia.csv")
vader_canada=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_canada.csv")
vader_india=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_india.csv")
vader_uk=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_uk.csv")
vader_us=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_us.csv")

for x in vader_australia.text:
	print(x["neg"])


print(vader_australia.head())