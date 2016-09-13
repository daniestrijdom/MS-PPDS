import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")

df = pd.read_sql_table('rates', engine, columns=['id','usd','repo','eur'])


#print df.loc[0:5,['usd','eur']]
print df.dtypes
