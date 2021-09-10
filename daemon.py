from config import Config
from techloan import Techloan
from spotseeker import Spots
import utils

config = {
    'SS_WEB_SERVER_HOST': 'http://localhost:8000',
    'SS_WEB_OAUTH_KEY': '',
    'SS_WEB_OAUTH_SECRET': '',
}

techloan = Techloan.from_fetch()
spots = Spots.from_spotseeker_server(config)

# def sync_equipment_to_item(equipment, item):
#     if equipment["name"]:
#         item["name"] = equipment["name"][:50]

#     item["category"] = equipment["_embedded"]["class"]["category"]
#     item["subcategory"] = equipment["_embedded"]["class"]["name"]

#     if equipment["description"]:
#         item["extended_info"]["i_description"] = utils.clean_html(equipment["description"][:350])
#     item["extended_info"]["i_brand"] = equipment["make"]
#     item["extended_info"]["i_model"] = equipment["model"]
#     if equipment["manual_url"]:
#         item["extended_info"]["i_manual_url"] = equipment["manual_url"]
#     item["extended_info"]["i_checkout_period"] = equipment["check_out_days"]
#     if equipment["stf_funded"]:
#         item["extended_info"]["i_is_stf"] = "true"
#     else:
#         item["extended_info"].pop("i_is_stf", None)
#     item["extended_info"]["i_quantity"] = equipment["num_active"]
#     item["extended_info"]["i_num_available"] = \
#         equipment["_embedded"]["availability"][0]["num_available"]

#     if equipment["reservable"]:
#         item["extended_info"]["i_reservation_required"] = "true"
#     else:
#         item["extended_info"].pop("i_reservation_required", None)
#     item["extended_info"]["i_access_limit_role"] = "true"
#     item["extended_info"]["i_access_role_students"] = "true"

# for spot in spots:
#     spot.deactive_all_items()
#     equipments = techloan_data.equipments_for_spot(spot)
#     for equipment in equipments:
#         item = spot.item_with_equipment_id(equipment['id'])

#         if item is None:
#             make = equipment['make']
#             model = equipment['model']
#             check_out_days = equipment['check_out_days']
#             item = {
#                 'name': "%s %s (%d day)" % (make, model, check_out_days),
#                 'category': '',
#                 'subcategory': '',
#                 'extended_info': {
#                     'cte_type_id': equipment["id"],
#                 },
#             }
#             item["name"] = item["name"][:50]
#             spot.append_item(item)

#         item["extended_info"]["i_is_active"] = "true"
#         sync_equipment_to_item(equipment, item)

spots.sync_with_techloan(techloan)

spots.upload_data()