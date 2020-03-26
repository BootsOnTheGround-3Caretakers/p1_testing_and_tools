from __future__ import unicode_literals, print_function
import requests
import json

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

params = {}
params['transaction_user_uid'] = "1"

service0 = {}
service0['name'] = "p1s1t6-create-caretaker-skill"
service0['PMA'] = {
    'p1s1t6_name': "electronics",
    'p1s1t6_description': "Fixing Electronic Appliances",
    'p1s1t6_skill_type': 'a',
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
