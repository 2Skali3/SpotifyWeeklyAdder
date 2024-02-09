import spotipy
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask, request, url_for, session, redirect

# aiuta ad automatizzare tutto
# a quanto pare flask fa in modo che tu accedi una volta e poi continua lui a creare sessioni nuove senza che debba farlo i
app = Flask(__name__)

# il nome del cookie è casuale scelto da me
app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'

# la chiave è randomica (ho messo delle lettere a caso). Serve solo a non far accedere gente strana.
app.secret_key = 'sdhfjklasldkfjhascvjhg'

TOKEN_INFO = 'token_info'

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')

@app.route('/saveDiscoverWeekly')

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "08bd1e1c056f40f98e495e625df3fae4",
        client_secret = "d698534528a64b829667aad23a818d7d",
        redirect_uri = url_for('redirect'), _external = True,
        scope = 'user-library-read playlist-modify-public playlist-modify-private'
    )