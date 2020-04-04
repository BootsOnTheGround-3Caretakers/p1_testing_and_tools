from __future__ import unicode_literals, print_function
import requests
import json
import time
from datetime import datetime

s4t1_task_sequence_list = 'p1s4t1_task_sequence_list'
s4t1_api_key = 'p1s4t1_api_key'


today = datetime.today().strftime('%m-%d')
test_name = "p1s2t1"
test_today = test_name+ "-" + today
params = {}
params['transaction_user_uid'] = "1"


#create user needer user
service0 = {}
service0['name'] = "p1s1t4-create-user"
service0['PMA'] = {
    'p1s1t4_first_name': "needer",
    'p1s1t4_last_name': test_today,
    'p1s1t4_phone_number': str(round(time.time())),
    'p1s1t4_firebase_uid': test_today + str(round(time.time())) + "_needer",
}
service0['RSA'] = {'p1s2t1_user_uid': 'uid',
                   'p1s1t5_user_uid': 'uid',
                   'p1s1t3_user_uid': 'uid'}

#create needer entry for new user
service1 = {}
service1['name'] = "p1s1t3-create-needer"
service1['PMA'] = {}
service1['RSA'] = {'p1s1t5_needer_uid': 'uid'}

#create cluster for new user
service2 = {}
service2['name'] = "p1s1t5-create-cluster"
service2['PMA'] = {"p1s1t5_expiration_date": str(round(time.time())+  10000)}
service2['RSA'] = {'p1s2t1_cluster_uid': 'uid'}

#add needer user to cluster
service3 = {}
service3['name'] = "p1s2t1-add-modify-cluster-user"
service3['PMA'] = {"p1s2t1_user_roles": "a"}

#create caretaker user
service4 = {}
service4['name'] = "p1s1t4-create-user"
service4['PMA'] = {
    'p1s1t4_first_name': "giver",
    'p1s1t4_last_name': test_today,
    'p1s1t4_phone_number': str(round(time.time())+ 1),
    'p1s1t4_firebase_uid': test_today  + str(round(time.time())) + "_giver",
}
service4['RSA'] = {'p1s2t1_user_uid': 'uid'}

#add caretaker user to cluster
service5 = {}
service5['name'] = "p1s2t1-add-modify-cluster-user"
service5['PMA'] = {"p1s2t1_user_roles": "b"}



 
data = {
    s4t1_api_key: 'BootsOnTheGround',
    s4t1_task_sequence_list: json.dumps([service0,service1,service2,service3,service4,service5]),
}

return_value = requests.post(
    'https://create-transaction-dot-aqueous-choir-160420.appspot.com/p1s4t1-create-external-transaction', data=data
)

print(return_value.status_code)
print(return_value.content)

