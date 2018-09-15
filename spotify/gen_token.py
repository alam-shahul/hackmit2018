import spotipy
from spotipy import oauth2

def gen_token():
    SPOTIPY_CLIENT_ID = '0179e2f900584c29acb09ce9ce1c9ef9'
    SPOTIPY_CLIENT_SECRET = '0669779d294e45a3b6071274aa026013'
    SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
    SCOPE = 'playlist-modify-public'
    CACHE = '.spotipyoauthcache'

    sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )
    
    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token")
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print("Found Spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']
    return access_token