from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
ids = data['Responder_id']
data_2 = pd.read_csv('data (1).csv')
ages = data_2['Age']
plt.style.use('fivethirtyeight')
# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins=bins, color='Red', edgecolor='black', log=True)
plt.axvline(x=29, color='black', linestyle='dashed', label='29 years old', linewidth=2)
plt.legend()
plt.title('Age Of Respondents')
plt.xlabel('Age')
plt.ylabel('Total Respondents')
plt.tight_layout()
plt.show()
