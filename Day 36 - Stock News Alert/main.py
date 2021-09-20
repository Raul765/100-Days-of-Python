import requests
import smtplib
import my_secrets

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = my_secrets.STOCK_KEY
NEWS_API_KEY = my_secrets.NEWS_KEY

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_parameters={
    "function": "TIME_SERIES_DAILY", 
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]

count=0
closing_prices=[]
for key in stock_data:
    if count<2:
        closing_price=float(stock_data[key]["4. close"])
        closing_prices.append(closing_price)
    else:
        break
change_pct = 100*(closing_prices[0]-closing_prices[1])/closing_prices[1]
print(change_pct)
        
## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

news_parameters={
    "q":COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

news_response=requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data=news_response.json()["articles"][0:2]
news_titles=[]
news_articles=[]
for article in news_data:
    news_titles.append(article["title"])
    news_articles.append(article["description"])

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

if abs(change_pct)>=5:
    MY_EMAIL = my_secrets.EMAIL
    MY_PASSWORD = my_secrets.PASSWORD
    SMTP_CONNECTION = "smtp.gmail.com"

    if change_pct > 0:
        subject=f"{STOCK} 🔺{abs(change_pct)}%"
    else:
        subject=f"{STOCK} 🔻{abs(change_pct)}%"

    with smtplib.SMTP(SMTP_CONNECTION) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addr=MY_EMAIL, msg=f"Subject:{subject} \n\nRelated articles: \nTitle: {news_titles[0]}\n Description: {news_articles[0]} \n\nTitle: {news_titles[1]}\n Description: {news_articles[1]} \n\nTitle: {news_titles[2]}\n Description: {news_articles[2]}")

#Optional: Format the SMS message like this: 
#"""
#TSLA: 🔺2%
#Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
#Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
#or
#"TSLA: 🔻5%
#Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
#Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
#"""

