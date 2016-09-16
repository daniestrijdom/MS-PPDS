from sklearn.datasets import load_iris
from pandas.tools.plotting import andrews_curves

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

data = load_iris()

df = pd.DataFrame(data.data, columns=data.feature_names)


for i in data.target:
    df['target_names'] = data.target_names[i]

'''
print df.head()
plt.figure()
andrews_curves(df, 'target_names')
plt.show()
'''
print df.corr()

plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
plt.show()
