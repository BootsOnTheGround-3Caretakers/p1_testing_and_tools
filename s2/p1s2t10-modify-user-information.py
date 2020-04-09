from __future__ import unicode_literals, print_function
import requests
import json
import time
from datetime import datetime

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

now = datetime.now()
time_str = now.strftime("%m%d%H%M%S")

test_name = "p1s2t10"
params = {
    'transaction_user_uid': '1',
}

services = [{
    'name': "p1s1t4-create-user",
    'PMA': {
        'p1s1t4_first_name': "firstname_{}_{}".format(test_name, time_str),
        'p1s1t4_last_name': "lastname_{}_{}".format(test_name, time_str),
        'p1s1t4_phone_number': str(round(time.time())),
        'p1s1t4_firebase_uid': "firebase_{}_{}".format(test_name, time_str),
        'p1s1t4_email_address': "email_{}_{}@example.com".format(test_name, time_str),
    },
    'RSA': {
        'p1s2t10_user_uid': 'uid'
    }
}, {
    'name': "p1s2t10-modify-user-information",
    'PMA': {
        "p1s2t10_first_name": "firstname2_{}_{}".format(test_name, time_str),
        "p1s2t10_last_name": "lastname2_{}_{}".format(test_name, time_str),
        "p1s2t10_country_uid": "US",
        "p1s2t10_region_uid": "0WtwHTADzxNxdEogI3ZX|1585555853",
        "p1s2t10_area_uid": "0072xmlHlCgII3DmSG88|1585562994",
        'p1s2t10_phone_number': str(int(time.time())),
        'p1s2t10_phone_texts': 'aaa',
        'p1s2t10_phone_2': str(int(time.time())),
        'p1s2t10_emergency_contact': str(int(time.time())),
        'p1s2t10_home_address': 'address {} {}'.format(test_name, time_str),
        'p1s2t10_email_address': "email_{}_{}@example.com".format(test_name, time_str),
        'p1s2t10_firebase_uid': "firebase_{}_{}".format(test_name, time_str),
        'p1s2t10_description': 'description {} {}'.format(test_name, time_str),
        'p1s2t10_preferred_radius': '1',
        'p1s2t10_account_flags': 'a',
        'p1s2t10_location_cord_lat': '41.8336474',
        'p1s2t10_location_cord_long': '-87.8723897',
    }
}]

data = {
    s4t1_api_key: 'BootsOnTheGround',
    s4t1_task_sequence_list: json.dumps(services),
}

return_value = requests.post(
    'https://create-transaction-dot-aqueous-choir-160420.appspot.com/p1s4t1-create-external-transaction', data=data
)

print(return_value.status_code)
print(return_value.content)
