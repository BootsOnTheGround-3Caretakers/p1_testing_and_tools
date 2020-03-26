from google.cloud import datastore
from google.cloud import ndb
import csv
import firebase_admin
from firebase_admin import credentials
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'accountAuth.json'

class RDK:
    success = "success"
    return_msg = "return_msg"
    debug_data = "debug_data"

class RC:
    success = True
    input_validation = 1001


def log_exception(function_name=None, action_description=None, exception_object=None):
    if type(function_name) != str:
        function_name = "Not Specified"
    if type(action_description) != str:
        action_description = "Not Specified"

    try:
        e_str = str(exception_object)
    except:
        e_str = "could not convert exception to string"

    output_string = 'expection occured in function: ' + function_name + '. while trying to: ' + action_description + ' .exception:' + e_str
    return output_string

#Done
def Dsp1SkillsSatisfiesNeeds():
    return_msg = "Dsp1SkillsSatisfiesNeeds:<Function>"
    debug_data = []
    call_result = {}

    try:
        client = datastore.Client()
    except Exception as error:
        return_msg += log_exception("Dsp1SkillsSatisfiesNeeds", "Function", error)
        return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}


    Dsp1Needs = ['Medical', 'Groceries', 'Transport', 'Videochat', 'Childcare', 'PetCare','CampingSpace', 'Water', 'SoapSanitation']


    for item in Dsp1Needs:
        key = client.key('Dsp1Needs', item)
        entity = datastore.Entity(key=key)
        entity.update({
            'need_uid': item,
        })
        client.put(entity)


    return {RDK.success: RC.success, RDK.return_msg: return_msg, RDK.debug_data: debug_data}


#client = ndb.Client()

#print(client)
#k = Dsp1Needs()
client = datastore.Client()
query = client.query()
query_iter = query.fetch()
for entity in query_iter:
    print(entity)
