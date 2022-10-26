#activity3
from lib2to3.pgen2.pgen import DFAState
import requests
import hashlib
import json
import pandas as pd
#importing libs


#defining keys

public_key='345207a1e6e10efb9acd4a5fceee4829'
private_key='08291be565ab98547bc23d1fe1e9e44b789aa3d3'
ts=1
hash= hashlib.md5((str(ts)+private_key+public_key).encode()).hexdigest()
address = 'https://gateway.marvel.com:443/v1/public/characters'

#defining parameters

parameters = {
    "apikey": public_key,
    "ts": ts,
    "hash": hash 
}

response =requests.get(address, params=parameters)
results = response.json()
print(json.dumps(results))

from string import ascii_lowercase
def df_characters(public_key,hash,nameStartsWith):
    for ch in list(ascii_lowercase):
        parameters={'ts':1,'apikey':public_key, 'hash':hash, 'nameStartsWith':nameStartsWith}
        response =requests.get(address, params=parameters)
    
        results = response.json()

        df=pd.json_normalize(results['data']['results'])
        df =df[['id','name','comics.available','events.available','stories.available','series.available']]
    return DFAState

def filter_char(df,column_name, filter_condition,filter_value):
    if column_name== 'name':
        filter_condition= 'starts_with'
        length =len(filter_value)
        return(df[df.name.str[:length]== filter_value])
    else:
        if filter_condition == 'equal_to':
            return(df[df[column_name]== int(filter_value)])
        elif filter_condition =='less_than':
            return(df[df[column_name]<int(filter_value)])
        elif filter_condition =='greater_than':
            return(df[df[column_name]>int(filter_value)])
        else:
            return('error')