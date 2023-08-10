import pandas as pd
import csv

df = pd.read_csv("Final.csv")

del df["Star_name2"]
del df["Distance2"]
del df["Mass2"]
del df["Radius2"]

df.to_csv('Final2.csv') 