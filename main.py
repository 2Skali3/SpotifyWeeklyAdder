import spotipy
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask, request, url_for, session, redirect

# aiuta ad automatizzare tutto
# a quanto pare flask fa in modo che tu accedi una volta e poi continua lui a creare sessioni nuove senza che debba farlo i
app = Flask(__name__)

# il nome del cookie è casuale scelto da me
app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'

# la chiave è randomica (ho messo delle lettere a caso. Serve solo a non far accedere gente strana.
app.secret_key = 'sdhfjklasldkfjhascvjhg'

TOKEN_INFO = 'token_info'

