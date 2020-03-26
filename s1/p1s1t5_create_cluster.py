from __future__ import unicode_literals, print_function
from datetime import datetime, timedelta
import time
import requests
import json

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

params = {}
params['transaction_user_uid'] = "1"

expiration_dt = datetime.now() + timedelta(days=7)
expiration_ts = int((time.mktime(expiration_dt.timetuple()) + expiration_dt.microsecond/1000000.0))

service0 = {}
service0['name'] = "p1s1t5-create-cluster"
service0['PMA'] = {
    'p1s1t5_user_uid': "123456",
    'p1s1t5_expiration_date': str(expiration_ts),
    'p1s1t5_needer_uid': "7891011",
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
