

import requests
#import json
import numpy as np




USER_AGENT = 'Mozilla/5.0'

def returnNameCombination(name1, name2):
    return callMeBaby()


def lastfm_get(payload, user):
    
    
    headers = {'user-agent': USER_AGENT}
    url = 'https://ws.audioscrobbler.com/2.0/'
    payload['api_key'] = user[0]
    payload['user'] = user[1]
    payload['format'] = 'json'
    
    response = requests.get(url, headers=headers, params=payload)
    
    return response


def callMeBaby():
    user = np.array(
             ['835defa77f6078c7a34c3c6ba04854c6', 'wuhuspringfield']
             #, ['ab8ab5b6deefd7b8afa5c1adab89fcb8', 'feybmertn']
             )
    page = 1
    limit = 2
    
    payload = {
                'method': 'user.getrecenttracks',
                'limit': limit,
                'page': page,
    }
    
    response = lastfm_get(payload, user)
    
    
    
    return (str(response.text))
