import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')

#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
#
# .. your code here ..

df = pd.read_csv("c:\users\\102012\desktop\courses\ms-ppds\module3\Datasets\wheat.data", index_col=None)
# print df.head()

#
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
#
# .. your code here ..

s1 = df[['area','perimeter']]
print s1.head()

#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
#
# .. your code here ..

s2 = df[['groove','asymmetry']]
print s2.head()

#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
#
# .. your code here ..

s1.plot.hist(alpha=0.75)
plt.show()

s2.plot.hist(alpha=0.75)
plt.show()
