'''
EXAMPLES FROM MODULE 3 - VISUALISATION
'''

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')
# NB - set index_col to 0th col if index already exists in dataset
df = pd.read_csv("students.data", index_col=0)

# NB: 2-D
df.plot.scatter(x='G1',y='G2')
plt.show()

# NB: 3-D
df.plot.scatter(x='G1',y='G2')
plt.show()
