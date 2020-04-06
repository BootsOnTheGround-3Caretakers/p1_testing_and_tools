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
service0['name'] = "p1s2t2-remove-user-from-cluster"
service0['PMA'] = {
    'p1s2t2_cluster_uid': '5244486082887680',
    'p1s2t2_user_uid': '4880523138695168',
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
