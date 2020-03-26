from google.cloud import datastore
from google.cloud import ndb
import csv
import firebase_admin
from firebase_admin import credentials
import os

#cred = credentials.Certificate("accountAuth.json")
#firebase_admin.initialize_app(cred)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'accountAuth.json'


Wd7MJhQb-create-code-to-populate-temporary-static-data-for-testing
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


#Reads the Zipcode into the US Region Name built in DsP1RegionCodes.py
def Dsp1AreaCodes():
    return_msg = "DsP1AreaCodes:<Function>"
    debug_data = []
    call_result = {}

    try:
        client = datastore.Client()
    except Exception as error:
        return_msg += log_exception("DsP1AreaCodes", "Function", error)
        return {RDK.success: RC.input_validation, RDK.return_msg: return_msg, RDK.debug_data: debug_data}

    #Read a list of Region Codes and match those with full name
    #Does this key format allow to put the zipcodes under the US Key? could not verify

    with open('zip_code_database.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            key = client.key('DsP1AreaCodes', 'US', row[1]) #Add Random String Generator)
            entity = datastore.Entity(key=key)
            entity.update({
                    'area_code': row[0],
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
