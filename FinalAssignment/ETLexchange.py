import glob
import pandas as pd
from datetime import datetime

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=['Name','Market Cap (US$ Billion)'])
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    
    return extracted_data


df = pd.read_csv('exchange_rates.csv')
exchange_rate = float(df[9:10]['Rates'])


def transform(data):
     data['Market Cap (US$ Billion)'] = round(0.75 * data['Market Cap (US$ Billion)'], 3)
     data.rename(columns={'Market Cap (US$ Billion)': 'Market Cap (GBP$ Billion)'}, inplace=True)  
     return data


def load(target_file, data_to_load):
    data_to_load.to_csv(target_file, index=False)

def log(message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y' #Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("\rate.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')


log("ETL Job Started")
log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")
log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")
log("Load phase Started")
load('market_cap.csv', transformed_data)
log("Load phase Ended")