from __future__ import unicode_literals, print_function
from datetime import datetime, timedelta
import time
import requests
import json

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

now = datetime.now()
today = datetime.today().strftime('%m-%d')
test_name = "p1s2t7"
test_today = test_name + "-" + today

params = {}
params['transaction_user_uid'] = "1"

service0 = {}
service0['name'] = "p1s1t4-create-user"
service0['PMA'] = {
    'p1s1t4_first_name': test_today,
    'p1s1t4_last_name': test_today,
    'p1s1t4_phone_number': str(round(time.time())),
    'p1s1t4_firebase_uid': test_today + str(round(time.time())),
}
service0['RSA'] = {
    'p1s2t7_user_uid': 'uid',
}

service1 = {}
service1['name'] = "p1s2t7-assign-hashtag-to-user"
service1['PMA'] = {
    'p1s2t7_hashtag_uid': '5672330625810432',
}

data = {
    s4t1_api_key: 'BootsOnTheGround',
    s4t1_task_sequence_list: json.dumps([service0, service1]),
}

return_value = requests.post(
    'https://create-transaction-dot-aqueous-choir-160420.appspot.com/p1s4t1-create-external-transaction', data=data
)

print(return_value.status_code)
print(return_value.content)
