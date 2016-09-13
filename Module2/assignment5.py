
import pandas as pd
import numpy as np


# TODO:
# Load up the dataset, setting correct header labels
# Use basic pandas commands to look through the dataset...
# get a feel for it before proceeding!
# Find out what value the dataset creators used to
# represent "nan" and ensure it's properly encoded as np.nan
#
# .. your code here ..

headers = ['a','education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']
df = pd.read_csv("Datasets\census.data", header=None)
df.columns = headers
df = df.drop('a',1)

df.fillna(np.nan)

# TODO:
# Figure out which features should be continuous + numeric
# Conert these to the appropriate data type as needed,
# that is, float64 or int64

# .. your code here ..
'''
seems to already be handled?
'''


# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal types using
# the method discussed in the chapter.
#
# .. your code here ..

'''
ordinal
- education?
- age buckets?
- hour buckets?
'''

# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any nominal types by
# exploding them out to new, separate, boolean fatures.
#
# .. your code here ..

'''
sex?
'''

df = pd.get_dummies(df, columns=[ 'race', 'sex', 'classification'])
# TODO:
# Print out your dataframe

print len(df.columns)
