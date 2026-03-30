import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from datetime import datetime, timedelta

plt.style.use('seaborn-v0_8-paper')
data = pd.read_csv("data_2.csv")
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values(by=['Date'], inplace=True)
price_date = data["Date"]
price_close = data["Close"]
plt.plot_date(price_date, price_close, linestyle='solid', marker='o', color='red', alpha=0.8)
plt.gcf().autofmt_xdate()
dates_format = mdates.DateFormatter('%b %d, %y')
plt.gca().xaxis.set_major_formatter(dates_format)
plt.title('Bitcoin Price')
plt.xlabel('Date')
plt.ylabel('Closing Bitcoin Price')
plt.tight_layout()
plt.grid(True)
plt.show()
# dates = [
#     datetime.today(),
#     datetime.today() + timedelta(days=1),
#     datetime.today() + timedelta(days=2),
#     datetime.today() + timedelta(days=3),
#     datetime.today() + timedelta(days=4),
#     datetime.today() + timedelta(days=5),
#     datetime.today() + timedelta(days=6),
#     datetime.today() + timedelta(days=7),
#     datetime.today() + timedelta(days=8),
#     datetime.today() + timedelta(days=9),
#     datetime.today() + timedelta(days=10),
#     datetime.today() + timedelta(days=11),
#     datetime.today() + timedelta(days=12),
# ]
# y = [1, 2, 3, 6, 5, 6, 7, 8, 9, 2, 11, 1, 13]
# plt.plot_date(dates, y, linestyle='solid', marker='o', color='red')
# plt.gcf().autofmt_xdate()
# dates_format = mdates.DateFormatter('%b %d, %Y')
