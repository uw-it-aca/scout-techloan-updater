from config import Config
from techloan import Techloan
from spotseeker import Spots
import utils

# TODO: set config
config = {
    'SS_WEB_SERVER_HOST': 'http://localhost:8000',
    'SS_WEB_OAUTH_KEY': '3972cc528611c615660dce3df49c2da5e549abb1',
    'SS_WEB_OAUTH_SECRET': 'EfCsi6OmKm3L9YvL',
    'SS_WEB_USER': 'demo_user',
}

techloan = Techloan.from_cte_api()
spots = Spots.from_spotseeker_server(config)

spots.sync_with_techloan(techloan)
spots.upload_data()