
import requests
import hashlib
import json
import pandas as pd
import sys


public_key = sys.argv[1]
nameStartsWith = sys.argv[2]
column_name = sys.argv[3]
filter_condition = sys.argv[4]
filter_value = sys.argv[5]

## Saving API data into variables
private_key = "08291be565ab98547bc23d1fe1e9e44b789aa3d3"
address = "https://gateway.marvel.com:443/v1/public/characters"
cts = 1
hash = hashlib.md5((str(charecters_ts)+private_key+public_key).encode()).hexdigest()
results_df = pd.DataFrame()


def create_dataframe(API_key, Hash, name_starts_with):
    charecters_df = pd.DataFrame()
    parameters = {
    "apikey" : API_key,
    "ts" : ts,
    "hash" : hash,
    "limit" : 100,
    "nameStartsWith" : name_starts_with }
    charecters_response = requests.get(address, params=parameters)
    charecters_results = charecters_response.json()
    df = pd.json_normalize(charecters_results['data'],['results'])
    df = df[['id','name','comics.available','events.available','stories.available','series.available']]
    charecters_df = charecters_df.append(df)
    return charecters_df

def filter_df(data_frame,column_name,filter_condition,filter_value):
    if column_name == "name":
        return(data_frame[data_frame.name.str[:len(filter_value)] == filter_value])
    if filter_condition == 'equal_to': 
        return(data_frame[data_frame[column_name] == filter_value])
    if filter_condition == 'less_than':
        return(data_frame[data_frame[column_name] < filter_value])
    if filter_condition == 'greater_than':
        return(data_frame[data_frame[column_name] > filter_value])
    return("Error")

results_df = create_dataframe(public_key,hash,nameStartsWith)
print(filter_df(results_df,column_name,filter_condition,filter_value))

