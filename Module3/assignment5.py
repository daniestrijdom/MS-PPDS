from pandas.tools.plotting import andrews_curves

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv("c:\users\\102012\desktop\courses\ms-ppds\module3\Datasets\wheat.data", index_col=None)

# df = df.drop(['id','area','perimeter'],axis=1)


# PART 2
plt.figure()
andrews_curves(df, 'wheat_type')
plt.show()
