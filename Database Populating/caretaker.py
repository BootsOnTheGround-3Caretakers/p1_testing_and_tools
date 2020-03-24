from google.cloud import datastore
import csv

client = datastore.Client()
key = client.key('DsP1CaretakerSkills')

with open('caretaker_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        entity = datastore.Entity(key=key)
        entity.update({
            'description': row['skill_name'],
            'skill_name': row['skill_name'],
            'skill_type': row['skill_type'],
        })
        client.put(entity)


print("Done")