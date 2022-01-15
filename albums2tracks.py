import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = 'YOUR_ID'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'YOUR_SECRET'

links = ['ALBUM','LINKS','HERE']
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

txtfile = open('tracklinks.txt', 'a')

for j in range(len(links)):
    results = spotify.album_tracks(links[j])
    # print(results)

    for i in range(len(results.get('items'))):
        ans = results.get('items')[i].get('uri')
        # print(ans)
        txtfile.writelines(ans)
        txtfile.writelines('\n')