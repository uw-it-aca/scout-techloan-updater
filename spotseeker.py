import json
import logging

# from authlib.integrations.base_client import OAuth2Session
import requests
from schema import Schema

logger = logging.getLogger(__name__)

class Spots:
    _scheme = Schema({
        'id': int,
        'name': str,
        'etag': str,
        'extended_info': {
            'cte_techloan_id': str,
        },
    }, ignore_extra_keys=True)
    
    _url = '{}/api/v1/spot/?extended_info:app_type=tech&extended_info:has_cte_techloan=true&limit=0'
    
    def __init__(self, spots):
        self.spots = []
        for spot in spots:
            try:
                self._scheme.validate(spot)
                self.spots.append(spot)
            except Exception as ex:
                logger.warning("Bad data retrieved from spotseeker " + str(ex) + " from " + json.dumps(spot))
    
    @classmethod
    def stringify_params(cls, params) -> str:
        def stringify_params(params, prepend) -> list[str]:
            if params is dict:
                params_str_array = []

                for key, item in params:
                    params_str_array.push(prepend + key + '=' + item)

                return params_str_array        

            return str(params)

        param_arr = stringify_params(params, '')
        
        return '?' + ('&'.join(param_arr))

    @classmethod
    def build_from_fetch(cls, hostname, params = {}) -> 'Spots':
        param_str = cls.stringify_params(params)
        
        spots = requests.get(cls._url.format(hostname)).json()
        return cls(spots)
    
def upload_data(config, spaces):
    # client = OAuth2Session(
    #     client_id=config.SS_WEB_OAUTH_KEY,
    #     client_secret=config.SS_WEB_OAUTH_SECRET,
    #     scope=config.SS_WEB_OAUTH_SCOPE,
    # )
    pass
    
    