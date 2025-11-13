import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10203569.csv', skiprows=4)

bangladesh = data[data['Country Name'] == 'Bangladesh']
years = list(range(1960, 2018))
gdp = bangladesh.loc[:, '1960':'2017'].values.flatten()

plt.plot(years, gdp, marker='o')
plt.xlabel('Year')
plt.ylabel('GDP (current US$)')
plt.title('Bangladesh GDP Over Time')
plt.grid(True)
plt.show()

