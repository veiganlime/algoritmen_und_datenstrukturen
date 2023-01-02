import pandas as pd
from  matplotlib  import pyplot as plt

dataframe = pd.read_csv('data/consolidated_coin_data.csv')

#print(dataframe.head(10))# erste 10 Zeilen von Dataset ausgeben
#print(dataframe.tail(10))# letzte 10 Zeilen von Dataset ausgeben
#print(dataframe)# erste und letzte 5 Zeilen von Dataset ausgeben
#print(dataframe.dtypes)# Datentypen abfragen
#print(dataframe.Currency.head) # einzelne Spalte(Serie) ausgeben
#print(dataframe.Currency.unique()) # alle Spalten(Serie) auflisten
#print(len(dataframe )) # Anzahl der Einträge ausgeben

dataframe = dataframe.loc[(dataframe['Currency'] == 'ethereum')]#Nach bestimmte Schlüsselwort suchen
#print(len(dataframe))#Anzahl vorhandenen Daten ausgeben

dataframe.loc[:,'Date'] = pd.to_datetime(dataframe.Date, format='%b %d, %Y')
dataframe.set_index('Date', inplace=True)
dataframe.describe()
print(dataframe.head(10))
dataframe['Close']=pd.to_numeric(dataframe['Close'], errors='coerce')

#plt.plot(dataframe.index, dataframe.Close)
#plt.show()

dataframe = dataframe.filter(items=['Close'])
print(dataframe.head(10))

for i in range(5):
    i = i + 6
    dataframe.loc[:,('Close' + str(i))] = dataframe.Close.shift(i)
print(dataframe.head(10))

new_dataframe = dataframe.dropna(axis = 0, how = 'any')
print(new_dataframe.head(10))
