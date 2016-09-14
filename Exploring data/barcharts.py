'''
EXAMPLES FROM MODULE 3 - VISUALISATION
ORDINAL DATA
'''

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')
# NB - set index_col to 0th col if index already exists in dataset
df = pd.read_csv("students.data", index_col=0)

series_a = df.G3
df_a = df[['G3','G2','G1']]

series_a.plot.hist(alpha=0.5)
plt.show()

df_a.plot.hist(alpha=0.5)
plt.show()
