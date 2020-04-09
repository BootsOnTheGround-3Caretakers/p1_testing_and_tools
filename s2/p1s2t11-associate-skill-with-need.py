from __future__ import unicode_literals, print_function
import requests
import json
from datetime import datetime


s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'

now = datetime.now()
time_str = now.strftime("%m%d%H%M%S")
test_name = "p1s2t11"
params = {
    'transaction_user_uid': "1",
}

services = [{
    'name': 'p1s1t1-create-need',
    'PMA': {
        'p1s1t1_name': "need_{}_{}".format(test_name, time_str),
        'p1s1t1_requirements': "requirements_{}_{}".format(test_name, time_str),
    },
    'RSA': {
        'p1s2t11_need_uid': 'uid'
    }
}, {
    'name': 'p1s1t6-create-caretaker-skill',
    'PMA': {
        'p1s1t6_name': "skill_{}_{}".format(test_name, time_str),
        'p1s1t6_description': "desc_{}_{}".format(test_name, time_str),
        'p1s1t6_skill_type': 'a',
    },
    'RSA': {
        'p1s2t11_skill_uid': 'uid'
    }
}, {
    'name': "p1s2t11-associate-skill-with-need",
    "PMA": {}
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
