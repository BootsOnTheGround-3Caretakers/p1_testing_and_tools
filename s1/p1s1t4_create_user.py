from __future__ import unicode_literals, print_function
import requests
import json
import time

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

params = {}
params['transaction_user_uid'] = "1"

service0 = {}
service0['name'] = "p1s1t4-create-user"
service0['PMA'] = {
    'p1s1t4_first_name': "first name 3/29",
    'p1s1t4_last_name': "last_name",
    'p1s1t4_phone_number': str(round(time.time())),
    'p1s1t4_firebase_uid': "firebase_uid",

}

data = {
    s4t1_api_key: 'BootsOnTheGround',
    s4t1_task_sequence_list: json.dumps([service0]),
}

return_value = requests.post(
    'https://create-transaction-dot-aqueous-choir-160420.appspot.com/p1s4t1-create-external-transaction', data=data
)

print(return_value.status_code)
print(return_value.content)
