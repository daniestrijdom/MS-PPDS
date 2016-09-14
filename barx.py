import pandas as pd
pd.options.mode.chained_assignment = None
import math

keepers = "https://barxffl.com/stats.aspx?page=playerSearch&t=1"
defenders = "https://barxffl.com/stats.aspx?page=playerSearch&t=2"
midfielders = "https://barxffl.com/stats.aspx?page=playerSearch&t=3"
forwards = "https://barxffl.com/stats.aspx?page=playerSearch&t=4"

df_k = pd.read_html(keepers)
df = df_k[0]

df_d = pd.read_html(defenders)
df = df.append(df_d[0],ignore_index=True)

df_m = pd.read_html(midfielders)
df = df.append(df_m[0],ignore_index=True)

df_f = pd.read_html(forwards)
df = df.append(df_f[0],ignore_index=True)

# TODO: remove players that have not played and those that have been scoring negative points
df = df[(df["Pld."]!=0) & (df['Pts.']>0)]
df = df.fillna(0)

# TODO: points per game & cost per point metrics, rank by ponts per game
df["pts/g"] = df["Pts."]/df["Pld."]
df['cost/p'] = df["Value"]/df["Pts."]/1000000

df =  df[df['Pld.'] >= math.floor(df['Pld.'].mean())].sort_values(by=("pts/g"), ascending=False)
df = df.reset_index(drop=True)

'''
print df[(df['Pos.']=="K") & (df['Pld.'] >= math.floor(df['Pld.'].mean()))].sort_values(by=("pts/g"), ascending=False).head()
print df[(df['Pos.']=="D") & (df['Pld.'] >= math.floor(df['Pld.'].mean()))].sort_values(by=("pts/g"), ascending=False).head()
print df[(df['Pos.']=="M") & (df['Pld.'] >= math.floor(df['Pld.'].mean()))].sort_values(by=("pts/g"), ascending=False).head()
print df[(df['Pos.']=="S") & (df['Pld.'] >= math.floor(df['Pld.'].mean()))].sort_values(by=("pts/g"), ascending=False).head()
'''

print df.head()

print df.tail()

print df.describe()


#TODO: test formations to see if less than 100K in value

#TODO: test formations
