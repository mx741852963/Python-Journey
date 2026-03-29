from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
key = ('JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java')
value = (59219, 55466, 47544, 36443, 35917)
explode = (0, 0, 0, 0.2, 0)
# plt.pie(slices, labels=le_1, colors=colors, wedgeprops={'edgecolor': 'Black'})
plt.pie(value, labels=key, wedgeprops={'edgecolor': 'Black'}, explode=explode, shadow=True, startangle=90,
        autopct="%1.1f%%")
plt.title('Pie Chart')
plt.tight_layout()
plt.show()
