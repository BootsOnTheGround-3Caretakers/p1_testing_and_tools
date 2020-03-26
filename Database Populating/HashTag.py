from google.cloud import datastore
import csv

client = datastore.Client()
key = client.key('DsP1HashTags')

hastags = ['#LGBTQ', '#HOMELESS', '#CHRISTIAN', '#VANLIFE', '#VETERANS', '#PREGNANT', '#NEWMOM', '#CANCER', '#FOSTERADOPTED', '#PROGRAMMERS', '#VEGANS', '#FOODALLERGIES', '#DANCERS', '#SIERRACLUB', '#NRA', '#DONATEBLOOD', '#DOGLOVERS', '#CATLOVERS', '#PETLOVERS', '#UCBERKELEY', '#STANFORD', '#CORNELL', '#BUDDHIST', '#MUSLIM', '#THAILAND', '#FILIPINO']


for tag in hastags:
    entity = datastore.Entity(key=key)
    entity.update({
        'description': tag,
        'name': tag,
    })
    client.put(entity)


print("Done")