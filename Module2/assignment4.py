import pandas as pd
import os

# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
source = "http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2"
os.environ["NO_PROXY"] = source

df = pd.read_html(source)

df = df[0]

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..

df.columns = df.iloc[1]
df = df[2::]
df = df.reset_index(drop=True)

# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..

df = df.dropna(axis=0, thresh=4)
df = df.reset_index(drop=True)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..

df = df[df.PTS.str.contains("PTS") == False]
df = df.reset_index(drop=True)


# TODO: Get rid of the 'RK' column
#
# .. your code here ..

df = df.drop('RK',1)


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..

df = df.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric

#TRIED TO MAKE A LOOP



for elem in df.columns[2:]:
    col = str(elem)

    try:
        df[col] = pd.to_numeric(df[col], errors="coerse")
    except:
        pass



# TODO: Your dataframe is now ready! Use the appropriate
# commands to answer the questions on the course lab page.

print len(df)
print len(df["PCT"].unique())
print df["GP"][15]+df["GP"][16]
