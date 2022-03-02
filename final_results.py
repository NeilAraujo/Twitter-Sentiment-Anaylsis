import pandas as pd
import json
import ast
import operator
import matplotlib.pyplot as plt

india= 17000000
us=62550000
canada=5800000
uk=15250000
australia=4600000

avg=21040000

india_fac= 0.807
us_fac= 2.97
can_fac=0.27
uk_fac=0.72
aus_fac=0.218

plt_india={}
plt_us={}
plt_uk={}
plt_canada={}
plt_aus={}

def mean_sentiment(data):
	pos=0
	neg=0
	neutral=0
	mean=0
	for i in data.text:
		x=ast.literal_eval(i)['compound']
		mean=mean+x
		if x>=0.05:
			pos=pos+1
		elif x<=-0.05:
			neg=neg+1
		else:
			neutral=neutral+1
	res={"pos":pos,"neg":neg,"neu":neutral}
	mean=x/data.shape[0]
	return mean,res

australia=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\sentiment_values\\sentiment_australia.csv")
canada=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\sentiment_values\\sentiment_canada.csv")
india=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\sentiment_values\\sentiment_india.csv")
uk=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\sentiment_values\\sentiment_uk.csv")
us=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\sentiment_values\\sentiment_us.csv")

vader_australia=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_australia.csv")
vader_canada=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_canada.csv")
vader_india=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_india.csv")
vader_uk=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_uk.csv")
vader_us=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\vader_sentiment_values\\sentiment_us.csv")

txt_australia=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\textblob_sentiment_values\\sentiment_australia.csv")
txt_canada=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\textblob_sentiment_values\\sentiment_canada.csv")
txt_india=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\textblob_sentiment_values\\sentiment_india.csv")
txt_uk=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\textblob_sentiment_values\\sentiment_uk.csv")
txt_us=pd.read_csv("C:\\Users\\Neil Araujo\\Documents\\webmining\\tweet_analysis\\textblob_sentiment_values\\sentiment_us.csv")


#print("With preprocessing")
result={}
result["Australia"],plt_aus=mean_sentiment(australia)
result["Canada"],plt_canada=mean_sentiment(canada)
result["India"],plt_india=mean_sentiment(india)
result["uk"],plt_uk=mean_sentiment(uk)
result["us"],plt_us=mean_sentiment(us)
sorted_result=dict(sorted(result.items(), key=operator.itemgetter(1),reverse=True))

result["Australia"]=result["Australia"]* -aus_fac;
result["Canada"]=result["Canada"]*-can_fac
result["India"]=result["India"]*-india_fac
result["uk"]=result["uk"]*-uk_fac
result["us"]=result["us"]*-us_fac


names = ['Australia', 'Canada', 'India' ,'us']
values = [result["Australia"],result["Canada"],result["India"],result["us"]]

plt.ylabel("Weighted value of negative sentiment in tweets")
plt.bar(names, values)
plt.show()

print(plt_india)
print(plt_uk)
print(plt_us)
print(plt_aus)
print(plt_canada)



print("Without preprocessing")
resulttwo={}
print("")
a={}
b={}
c={}
d={}
e={}
resulttwo["Australia"],a=mean_sentiment(vader_australia)
resulttwo["Canada"],b=mean_sentiment(vader_canada)
resulttwo["India"],c=mean_sentiment(vader_india)
resulttwo["uk"],d=mean_sentiment(vader_uk)
resulttwo["us"],e=mean_sentiment(vader_us)

resulttwo["Australia"]=resulttwo["Australia"]* -aus_fac;
resulttwo["Canada"]=resulttwo["Canada"]*-can_fac
resulttwo["India"]=resulttwo["India"]*-india_fac
resulttwo["uk"]=resulttwo["uk"]*-uk_fac
resulttwo["us"]=resulttwo["us"]*-us_fac

namestwo = ['Australia', 'Canada', 'India' ,'us']
valuestwo = [resulttwo["Australia"],resulttwo["Canada"],resulttwo["India"],resulttwo["us"]]

plt.ylabel("Weighted value of negative sentiment in tweets")
plt.bar(names,values)
plt.bar(namestwo, valuestwo)
plt.show()


print("Textblob")
resultthree={}
l={}
m={}
n={}
o={}
p={}
resultthree["Australia"],l=mean_sentiment(txt_australia)
resultthree["Canada"],m=mean_sentiment(txt_canada)
resultthree["India"],n=mean_sentiment(txt_india)
resultthree["uk"],o=mean_sentiment(txt_uk)
resultthree["us"],p=mean_sentiment(txt_us)

resultthree["Australia"]=resultthree["Australia"]* -aus_fac;
resultthree["Canada"]=resultthree["Canada"]*-can_fac
resultthree["India"]=resultthree["India"]*-india_fac
resultthree["uk"]=resultthree["uk"]*-uk_fac
resultthree["us"]=resultthree["us"]*-us_fac

namesthree = ['Australia', 'Canada', 'India' ,'us']
valuesthree = [resultthree["Australia"],resultthree["Canada"],resultthree["India"],resultthree["us"]]




fig, (ax1, ax2) = plt.subplots(1, 3)
fig.suptitle('Difference when captilization, punctuation and emojis and mentained and when they are not')
ax1.bar(names,values)
ax2.bar(namestwo,valuestwo)
ax3.bar(namesthree,namesthree)
plt.show()


