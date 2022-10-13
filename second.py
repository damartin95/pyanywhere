

import requests
#import json
import numpy as np
import pandas as pd




USER_AGENT = 'Mozilla/5.0'

def returnNameCombination(name1, name2):
    return callMeBaby(name1, name2)


def lastfm_get(payload, user):
    
    
    headers = {'user-agent': USER_AGENT}
    url = 'https://ws.audioscrobbler.com/2.0/'
    payload['api_key'] = user[0]
    payload['user'] = user[1]
    payload['format'] = 'json'
    
    response = requests.get(url, headers=headers, params=payload)
    
    return response


def callMeBaby(name1, name2):
    user = np.array(
             [name1, name2]
             #, ['ab8ab5b6deefd7b8afa5c1adab89fcb8', 'feybmertn']
             )
    page = 1
    limit = 1
    
    payload = {
                'method': 'user.getrecenttracks',
                'limit': limit,
                'page': page,
    }
    
    response = lastfm_get(payload, user)
    
    responses_df = []
    
        
    single_response_json = response.json()
    single_response_track = single_response_json['recenttracks']['track']
        
        
    responses_df.append(single_response_track)
    
    
    r0_df = pd.concat([pd.DataFrame(i) for i in responses_df], ignore_index=True)
    

    
    print('0', r0_df)
    
    if 1==1:
        r0_df = r0_df.drop('image', axis=1)
        print('1', r0_df)
        r0_df = r0_df.drop('streamable', axis=1)
        r0_df = r0_df.drop('url', axis=1)
        print('2', r0_df)
        #r0_df = r0_df.drop('mbid', axis=1) # musicbrainz id = unique identifier
        r0_df['artist'] = r0_df.artist.astype(str)
        r0_df['album'] = r0_df.album.astype(str)
        r0_df['date'] = r0_df.date.astype(str)
        print('3', r0_df)
        
        r0_df[['mbid2','new_artist']]=r0_df['artist'].str.split("#text':", n = 1, expand = True)
        r0_df = r0_df.drop('mbid2', axis=1)
        r0_df = r0_df.drop('artist', axis=1)
        
        print('4', r0_df)
        r0_df[['mbid3','new_album']]=r0_df['album'].str.split("#text':", n = 1, expand = True)
        r0_df = r0_df.drop('mbid3', axis=1)
        r0_df = r0_df.drop('album', axis=1)
        r0_df[['uts','new_date']]=r0_df['date'].str.split("#text':", n = 1, expand = True)
        r0_df = r0_df.drop('date', axis=1)
        print('5', r0_df)
        
        r0_df = r0_df.drop('uts', axis=1) ## UTS
        
        
        if '@attr' in r0_df.columns: 
            r0_df = r0_df.drop('@attr', axis=1) # this fucker only shows up when a song is being played
            r0_df = r0_df.iloc[1:] # removed the top row as it contains None in its 'Date' column
    
        print('6', r0_df)
        r0_df['new_artist'] = r0_df['new_artist'].str[2:-2]
        r0_df['new_album'] = r0_df['new_album'].str[2:-2]
        r0_df['new_date'] = r0_df['new_date'].str[2:-2]
    
    
        #r0_df = r0_df.fillna(value=np.nan)
        
        

    
       
    if 1==1: # PREPARE DATES
        r0_df['Date'] = pd.to_datetime(r0_df['new_date'])
        r0_df = r0_df.drop('new_date', axis=1)  
        
        #print(r0_df.head())
        
        r0_df['Year'] = pd.DatetimeIndex(r0_df['Date']).year
        r0_df['Month'] = pd.DatetimeIndex(r0_df['Date']).month
         
      
    r0_df.columns=['mbid', 'Song','Artist','Album','Date', 'Year', 'Month']
    
    
    return (str('Dis bisch listened to ' + r0_df['Song'][0] + ' by ' + r0_df['Artist'][0]))
