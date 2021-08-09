from config import Config
import techloan
import spotseeker

config = {
    'SS_WEB_SERVER_HOST': 'http://localhost:8000',
    'SS_WEB_OAUTH_KEY': '',
    'SS_WEB_OAUTH_SECRET': '',
}

techloan.Techloan.from_fetch()
spotseeker.Spots.from_fetch(config['SS_WEB_SERVER_HOST'])