import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
#
# .. your code here ..

df = pd.read_csv("c:\users\\102012\desktop\courses\ms-ppds\module3\Datasets\wheat.data", index_col=None)

#
# TODO: Drop the 'id' feature
#
# .. your code here ..
df = df.drop(['id'],axis=1)

#
# TODO: Compute the correlation matrix of your dataframe
#
# .. your code here ..

corr = df.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
#
# .. your code here ..
print corr
plt.imshow(corr, cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
plt.show()
