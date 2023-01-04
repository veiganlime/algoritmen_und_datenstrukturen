import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#csv file importieren und vorbereiten
dataframe = pd.read_csv('data/consolidated_coin_data.csv')
dataframe = dataframe.loc[(dataframe['Currency'] == 'ethereum')]#bestimmte Währung aussortieren
dataframe['Close']=pd.to_numeric(dataframe['Close'], errors='coerce')#Preis in nummericshe Werte umwandlen
dataframe.loc[:,'Date'] = pd.to_datetime(dataframe.Date, format='%b %d, %Y')# Date in Dateformat umwandlen
dataframe.set_index('Date', inplace=True)# Für jeden Date index zuordnen

dataframe = dataframe.filter(items=['Close'])#für den ausgewählten
dataframe['Time'] = np.arange((len(dataframe.index)))


dataframe.describe()
print(dataframe.head())
print(dataframe.dtypes)


#def loss_function(m, b, points):
#    total_error = 0
#    for i in range (len(points)):
#        x = points.iloc[i].Date
#        y = points.iloc[i].Close
#        total_error += (y-(m * x + b)) ** 2
#    total_error / float(len(points))


def gradient_descent(m_now, b_now, points, l):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].Time
        y = points.iloc[i].Close

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * l
    b = b_now - b_gradient * l
    return m, b


m = 0
b = 0
l = 0.0001
iteration = 500

for i in range(iteration):
    if i % 50 == 0:
        print(f"iteration: {i}")
    m, b = gradient_descent(m, b, dataframe, l)

print(m, b)

plt.scatter(dataframe.index, dataframe.Close, color="black")
plt.plot(list(range(20,80)), [m * x +b for x in range(20, 80)], color="red")
plt.show()
