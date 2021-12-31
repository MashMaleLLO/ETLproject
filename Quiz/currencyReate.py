import requests
import pandas as pd

url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=6090903f2543df65d7798168d8d46dae"  #Make sure to change ******* to your API key.
req = requests.get(url)
data = req.json()

df = pd.DataFrame(data, columns=['rates'])

df = df.to_csv(r'exchange_rates_1.csv')