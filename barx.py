'''
# Module that will create a pandas dataframe object with player statistics
'''

def barx_df():
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
    df['cost/p/game'] = df["Value"]/df["pts/g"]/1000000

    # TODO: fair-value
    # add fair value metric by comparing valuation quantile to
    # points quantile, return bolean value

    df =  df[df['Pld.'] >= math.floor(df['Pld.'].mean())].sort_values(by=("pts/g"), ascending=False)
    df = df.reset_index(drop=True)

    '''
    print df[(df['Pos.']=="K") & (df['Pld.'] >= math.floor(df['Pld.'].mean()))].sort_values(by=("pts/g"), ascending=False).head()
    print df[(df['Pos.']=="D") & (df['Pld.'] >= math.floor(df['Pld.'].mean()))].sort_values(by=("pts/g"), ascending=False).head()
    print df[(df['Pos.']=="M") & (df['Pld.'] >= math.floor(df['Pld.'].mean()))].sort_values(by=("pts/g"), ascending=False).head()
    print df[(df['Pos.']=="S") & (df['Pld.'] >= math.floor(df['Pld.'].mean()))].sort_values(by=("pts/g"), ascending=False).head()
    '''


    import matplotlib
    import matplotlib.pyplot as plt

    plt.style.use('ggplot')
    df.plot.scatter(x='pts/g',y='cost/p/game', marker=".")

    for i in range(len(df)):
        plt.annotate(df['Player'][i], xy=(df['pts/g'][i],df['cost/p/game'][i]), xytext=(df['pts/g'][i],df['cost/p/game'][i]))

    plt.show()

    return df

if __name__ == "__main__":
    barx = barx_df()
    barx = barx[["Pos.","Player","Club","Value","pts/g"]]

    print "\nBEST------\n", barx.head(30)
    #print "\nWORST------\n", barx.tail(10)
