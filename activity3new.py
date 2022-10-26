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

df_characters(public_key,hash,'a')