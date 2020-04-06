from __future__ import unicode_literals, print_function
from datetime import datetime, timedelta
import time
import requests
import json

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

params = {}
params['transaction_user_uid'] = "1"

service0 = {}
service0['name'] = "p1s2t9-remove-skill-from-user"
service0['PMA'] = {
    'p1s2t9_user_uid': '5650034074845184',
    'p1s2t9_skill_uid': '5685265389584384',
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
