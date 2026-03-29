from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
language_counter = Counter()
for response in lang_responses:
    language_counter.update(response.split(';'))
data_x = language_counter.most_common(15)
keys, values = zip(*data_x)
plt.style.use('seaborn-v0_8-dark')
plt.title("Language Count by  population")
plt.xlabel("Languages")
plt.ylabel("Population")
plt.legend()
plt.barh(keys, values)
plt.tight_layout()
plt.grid()
plt.show()
