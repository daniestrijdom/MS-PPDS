import pandas as pd

keepers = "https://barxffl.com/stats.aspx?page=playerSearch&t=1"
defenders = "https://barxffl.com/stats.aspx?page=playerSearch&t=2"
midfielders = "https://barxffl.com/stats.aspx?page=playerSearch&t=3"
forwards = "https://barxffl.com/stats.aspx?page=playerSearch&t=4"

df_k = pd.read_html(keepers)
df_p = df_k[0]

df_d = pd.read_html(defenders)
df_p = df_p.append(df_d[0],ignore_index=True)

df_m = pd.read_html(midfielders)
df_p = df_p.append(df_m[0],ignore_index=True)

df_f = pd.read_html(forwards)
df_p = df_p.append(df_f[0],ignore_index=True)

df = df_p
df = df[(df["Pld."]!=0) & (df['Pts.']>0)]

#TODO: points per game & cost per point metrics
df["pts/g"] = df["Pts."]/df["Pld."]
df["cost/pt"] = df["Value"]/df["Pts."]/1000000

# print df[(df["pts/g"]>df["pts/g"].mean()) & (df["Pld."]==4)]
print df[df['Pos.']=="K"].sort(columns=["pts/g"], ascending=False).head()
print df[df['Pos.']=="D"].sort(columns=["pts/g"], ascending=False).head()
print df[df['Pos.']=="M"].sort(columns=["pts/g"], ascending=False).head()
print df[df['Pos.']=="S"].sort(columns=["pts/g"], ascending=False).head()


#TODO: test formations to see if less than 100K in value

#TODO: test formations
