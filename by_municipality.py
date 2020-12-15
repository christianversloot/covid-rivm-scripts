import pandas as pd
import requests
import io
import time
import sys
import datetime

# Prepare request
url = 'https://data.rivm.nl/covid-19/COVID-19_aantallen_gemeente_per_dag.csv'
params = {}

# Prepare dates
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(hours=24)
today = today.strftime("%Y-%m-%d") # e.g. '2020-10-20'
yesterday = yesterday.strftime("%Y-%m-%d") # e.g. '2020-10-19

# Prepare city
municipalities =  ['Amsterdam', 'Rozendaal', 'Rotterdam', 'Urk', 'Nijmegen', 'Deventer', 'Utrecht', 'Apeldoorn', '\'s-Gravenhage', 'Steenbergen', 'Bergen op Zoom', '\'s-Hertogenbosch', 'Enschede']
print('Getting data')
r = requests.get(url,data=params)
if r.ok:
  print('Data received')
  data = r.content.decode('utf8')
  df = pd.read_csv(io.StringIO(data), delimiter=';')
  df_y = df[df['Date_of_publication'] == yesterday]
  df = df[df['Date_of_publication'] == today]
  for municipality in municipalities:
    df_c_y = df_y[df_y['Municipality_name'] == municipality]
    df_c = df[df['Municipality_name'] == municipality]
    summed = df_c['Total_reported'].sum()
    summed_y = df_c_y['Total_reported'].sum()
    print(f'Number of cases in municipality {municipality} on {today} = {summed}')
    print(f'Number of cases in municipality {municipality} on {yesterday} = {summed_y}')