from __future__ import unicode_literals, print_function
import requests
import json
import time
from datetime import datetime

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'


today = datetime.today().strftime('%m-%d')
test_name = "p1s2t3"
test_today = test_name+ "-" + today
params = {}
params['transaction_user_uid'] = "1"


#create user 
service0 = {}
service0['name'] = "p1s1t4-create-user"
service0['PMA'] = {
    'p1s1t4_first_name': test_today,
    'p1s1t4_last_name': test_today,
    'p1s1t4_phone_number': str(round(time.time())),
    'p1s1t4_firebase_uid': test_today + str(round(time.time())),
}
service0['RSA'] = {'p1s2t3_user_uid': 'uid'}

#create skill
service1 = {}
service1['name'] = "p1s1t6-create-caretaker-skill"
service1['PMA'] = {
    "p1s1t6_name": test_today + str(round(time.time())),
    "p1s1t6_description": test_today + str(round(time.time())),
    "p1s1t6_skill_type": "bc"
}
service1['RSA'] = {'p1s2t3_skill_uid': 'uid'}

#assign skill to user
service2 = {}
service2['name'] = "p1s2t3-add-modify-user-skill"
service2['PMA'] = {
    "p1s2t3_special_notes": test_today + str(round(time.time())),
    "p1s2t3_total_capacity": 1
}


data = {
    s4t1_api_key: 'BootsOnTheGround',
    s4t1_task_sequence_list: json.dumps([service0,service1,service2]),
}

return_value = requests.post(
    'https://create-transaction-dot-aqueous-choir-160420.appspot.com/p1s4t1-create-external-transaction', data=data
)

print(return_value.status_code)
print(return_value.content)

