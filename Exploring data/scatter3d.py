'''
EXAMPLES FROM MODULE 3 - VISUALISATION
'''

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('ggplot')
# NB - set index_col to 0th col if index already exists in dataset
df = pd.read_csv("students.data", index_col=0)

# INIT PLOT OBJECT
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel("Final Grade")
ax.set_ylabel("First Grade")
ax.set_zlabel("Daily Alcohol")

ax.scatter(df.G1,df.G3,df.Dalc, c='r', marker=".")
plt.show()
