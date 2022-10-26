#activity 2

import requests
import hashlib
import json
import pandas as pd
#importing libs


#defining keys and address

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
#first api call

#fetch all the charecters by a for loop

from string import ascii_lowercase


charecters_df =pd.DataFrame()

for ch in list(ascii_lowercase):
    parameters={'ts':1,'apikey':public_key, 'hash':hash,'limit':100, 'nameStartsWith':ch}
    response =requests.get(address, params=parameters)
    results = response.json()
    df=pd.json_normalize(results['data']['results'])
    df =df[['id','name','comics.available','events.available','stories.available','series.available']]
    charecters_df=charecters_df.append(df)