import json
import logging
from typing import Iterator

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
    
    def __init__(self, equipments):
        self.equipments = []
        for equipment in equipments:
            try:
                self._scheme.validate(equipment)
                self.equipments.append(equipment)
            except Exception as ex:
                logger.warning("Bad data retrieved from the techloan " + str(ex) + " from " + json.dumps(equipment))

    def equipments_for_spot(self, spot) -> Iterator:
        return filter(
            lambda equipment: equipment["equipment_location_id"] == int(spot["extended_info"]["cte_techloan_id"]),
            self.equipments,
        )

    @classmethod
    def from_cte_api(cls) -> 'Techloan':
        equipments = requests.get(cls._url).json()
        return cls(equipments)
        