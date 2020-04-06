from __future__ import unicode_literals, print_function
from datetime import datetime, timedelta
import time
import requests
import json

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

now = datetime.now()
today = datetime.today().strftime('%m-%d')
test_name = "p1s2t3"
test_today = test_name+ "-" + today

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
    'p1s1t3_user_uid': 'uid',
    'p1s2t4_user_uid': 'uid',
}

service1 = {}
service1['name'] = "p1s1t1-create-need"
service1['PMA'] = {
    'p1s1t1_name': "wheelchair {}".format(now),
    'p1s1t1_requirements': "manual {}".format(now),
}
service1['RSA'] = {'p1s2t4_need_uid': 'uid'}

service2 = {}
service2['name'] = "p1s1t3-create-needer"
service2['PMA'] = {
}
service2['RSA'] = {'p1s2t4_needer_uid': 'uid'}

service4 = {}
service4['name'] = "p1s2t4-add-modify-need-to-needer"
service4['PMA'] = {
    'p1s2t4_special_requests': 'Please add a plastic spoon',
}

data = {
    s4t1_api_key: 'BootsOnTheGround',
    s4t1_task_sequence_list: json.dumps([service0, service1, service2, service4]),
}

return_value = requests.post(
    'https://create-transaction-dot-aqueous-choir-160420.appspot.com/p1s4t1-create-external-transaction', data=data
)

print(return_value.status_code)
print(return_value.content)
