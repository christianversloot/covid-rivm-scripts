import pandas as pd
import requests
import io
from playsound import playsound
import time
import sys
import datetime

# Prepare request
url = 'https://data.rivm.nl/covid-19/COVID-19_aantallen_gemeente_per_dag.csv'
params = {}

# Prepare dates
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(hours=24)
date = today.strftime("%Y-%m-%d") # e.g. '2020-10-20'
yesterday = yesterday.strftime("%Y-%m-%d") # e.g. '2020-10-19

# Prepare some variables
summed = 0
higher = False
equal = False
difference = 0
differencename = ""

# Loop
while True:
    print('====================================================')
    print('Getting new data')
    r = requests.get(url,data=params)
    if r.ok:
      print('Data received')
      lgt = 0
      data = r.content.decode('utf8')
      df = pd.read_csv(io.StringIO(data), delimiter=';')
      df_y = df[df['Date_of_publication'] == yesterday]
      df = df[df['Date_of_publication'] == date]
      summed = df['Total_reported'].sum()
      summed_y = df_y['Total_reported'].sum()
      print(f'Check - number of rows: today = {summed} / yesterday = {summed_y}')
      lgt = len(df)
      if lgt > 0:
        print('New data!')
        higher = summed > summed_y
        equal = summed == summed_y
        difference = abs(summed - summed_y)
        differencename = "gelijk" if equal else "minder"
        differencename = "meer" if higher else "minder"
        break
      else:
        print('Nothing known, sleeping 20 seconds')
        time.sleep(20)
    else:
        print('Nothing known, sleeping 20 seconds')
        time.sleep(20)

print('====================================================')
print(f'Aantal besmettingen op {date} = {summed}')
print(f'Verschil: {difference} {differencename}')
playsound('./alarm.mp3')