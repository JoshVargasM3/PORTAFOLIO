#To analize data we need to import the respectly libraries.
import pandas as pd
import numpy as np

url ="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header= None)

df.head()
df.describe()
df.describe()
df.info()
df.head(5)
df.tail(10)

#we have to add headers manually.

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
        "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
        "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
        "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.head(10)
df.describe()
#We need to replace the "?" symbol with NaN so the dropna() can remove the missing values to clean the data.
df1=df.replace('?', 'NaN') 
df=df1.dropna(subset=["price"], axis=0)
df.head(20)
print(df.columns)

# if you would save the dataframe df as automobile.csv to your local machine.
df.to_csv("automobile.csv", index=False) 
print(df.dtypes)

df.describe(include = "all") 

#Where "column" is the name of the column, you can apply the method ".describe()" to get the statistics of                            those columns as follows: dataframe[[' column 1 ',column 2', 'column 3'] ].describe()
df[['length', 'compression-ratio']].describe()