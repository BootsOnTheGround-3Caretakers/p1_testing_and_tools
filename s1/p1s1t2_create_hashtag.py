from __future__ import unicode_literals, print_function
import requests
import json

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

params = {}
params['transaction_user_uid'] = "1"

service0 = {}
service0['name'] = "p1s1t2-create-hashtag"
service0['PMA'] = {
    'p1s1t2_name': "covid19emergency",
    'p1s1t2_description': "Symptoms have worsen significantly",
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
