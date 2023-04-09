import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import mplcursors
import plotly.express as px
import plotly.io as pio



df = pd.DataFrame()
df['SingleTrue'] = np.concatenate((np.repeat(0.6, 73), np.arange(6.6, 106, 6)))
df['SingleTrue'] = np.where(df['SingleTrue'] > 100, 100, df['SingleTrue'])
df['SingleFalse'] = np.where((100 - df['SingleTrue']) < 0, 0, 100 - df['SingleTrue'])
Cumprod = (df['SingleFalse'] / 100).cumprod()
df['FalseCumprod'] = Cumprod * 100

df['SingleTrue'].index += 1
df['SingleFalse'].index += 1
df['FalseCumprod'].index += 1
df['Pulls'] = df.index

#plt.subplot(3,1,1)
#plt.title('Odds to receive 5 star in a single pull')
#plt.scatter(df['SingleTrue'].index, df['SingleTrue'],
#            label = 'SingleTrue', color = 'g')
#plt.legend()
#
#plt.subplot(3,1,2)
#plt.title('Odds to not receive 5 star in a single pull')
#plt.scatter(df['SingleFalse'].index, df['SingleFalse'],
#            label = 'SingleFalse', color = 'r')
#plt.subplot(3,1,3)
#plt.title('Odds to not receive 5 star in cumlative pulls')
#plt.scatter(df['CumProd'].index, df['CumProd'],
#            label = 'CumProd', color = 'b')
#plt.legend()
#
#mplcursors.cursor(hover=True)
#plt.show()

fig = px.scatter(df, x = 'Pulls', y = 'SingleTrue', color = 'FalseCumprod', hover_data = 'SingleFalse')
fig.write_html("idk.html", auto_open = True)


