import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv('studentdata.csv')
a=df.loc[df['student_id']=="TRL_987"]
print(a)
print(a.groupby("level")['attempt'].mean())
fig=go.Figure(go.Bar(
    x=a.groupby("level")['attempt'].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'
))
fig.show()