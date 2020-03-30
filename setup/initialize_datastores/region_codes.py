from __future__ import print_function

import random
import string
import time

import pandas as pd
from google.cloud import datastore


def generate_region_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=20)) + '|' + str(int(time.time()))


def main():
    client = datastore.Client()

    region_dict = {}
    query = client.query(kind='DsP1RegionCodes')
    for entity in query.fetch():
        key = entity.key
        parent_key = key.parent
        if parent_key.name not in region_dict:
            region_dict[parent_key.name] = set()
        region_dict[parent_key.name].add(entity['region_code'])

    locations = [("US", "50_us_states_all_data.csv", "read_csv", None, 2, 1)]

    for loc in locations:
        country_code, region_file, read_method, header, code_index, name_index = loc

        df = getattr(pd, read_method)(region_file, header=header)
        for row in df.iterrows():
            fields = row[1]
            region_code = fields[code_index]
            region_name = fields[name_index]

            if country_code in region_dict and region_code in region_dict[country_code]:
                continue

            print("REGION:", region_code)
            region_key = client.key(
                'DsP1CountryCodes', country_code, 'DsP1RegionCodes', generate_region_id()
            )
            entity = datastore.Entity(key=region_key)
            entity['region_code'] = region_code
            entity['name'] = region_name
            client.put(entity)


if __name__ == '__main__':
    main()
