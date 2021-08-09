import json
import logging

import requests
from schema import Schema, Or

logger = logging.getLogger(__name__)

class Techloan:
    _scheme = Schema({
        'id': int,
        'name': Or(str, None),
        'description': Or(str, None),
        'equipment_location_id': int,
        'make': str,
        'model': str,
        'manual_url': Or(str, None),
        'image_url': str,
        'check_out_days': Or(int, None),
        'stf_funded': bool,
        'num_active': int,
        '_embedded': {
            'class': {
                'name': str,
                'category': str,
            },
            'availability': [{
                'num_available': int,
            }],
        },
    }, ignore_extra_keys=True)
    
    _url = 'https://www.cte.uw.edu/tools/techloan/api/v2/type/?embed=availability&embed=class'
    
    def __init__(self, entries):
        self.entries = []
        for entry in entries:
            try:
                self._scheme.validate(entry)
                self.entries.append(entry)
            except Exception as ex:
                logger.warning("Bad data retrieved from the techloan " + str(ex) + " from " + json.dumps(entry))
    
    @classmethod
    def from_fetch(cls) -> 'Techloan':
        entries = requests.get(cls._url).json()
        return cls(entries)
        