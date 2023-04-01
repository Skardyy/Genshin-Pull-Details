import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import mplcursors



df = pd.DataFrame()
df['SingleTrue'] = np.concatenate((np.repeat(0.6, 73), np.arange(6.6, 106, 6)))
df['SingleFalse'] = np.where((100 - df['SingleTrue']) < 0, 0, 100 - df['SingleTrue'])
Cumprod = (df['SingleFalse'] / 100).cumprod()
df['CumProd'] = Cumprod * 100

df['SingleTrue'].index += 1
df['SingleFalse'].index += 1
df['CumProd'].index += 1

plt.subplot(3,1,1)
plt.title('Odds to receive 5 star in a single pull')
plt.scatter(df['SingleTrue'].index, df['SingleTrue'],
            label = 'SingleTrue', color = 'g')
plt.plot(df['SingleTrue'].index, df['SingleTrue'],
         color = 'g')
plt.legend()

plt.subplot(3,1,2)
plt.title('Odds to not receive 5 star in a single pull')
plt.scatter(df['SingleFalse'].index, df['SingleFalse'],
            label = 'SingleFalse', color = 'r')
plt.plot(df['SingleFalse'].index, df['SingleFalse'],
         color = 'r')
plt.legend()

plt.subplot(3,1,3)
plt.title('Odds to not receive 5 star in cumlative pulls')
plt.scatter(df['CumProd'].index, df['CumProd'],
            label = 'CumProd', color = 'b')
plt.plot(df['CumProd'].index, df['CumProd'],
         color = 'b')
plt.legend()

mplcursors.cursor(hover=True)
plt.show()


