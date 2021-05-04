import pandas as pd
import csv
import plotly.figure_factory as pf

df =  pd.read_csv("data.csv")
fig = pf.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist = False)
fig.show()