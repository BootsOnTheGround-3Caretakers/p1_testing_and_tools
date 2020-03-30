from __future__ import print_function

import random
import string
import time

import pandas as pd
from google.cloud import datastore


def generate_area_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=20)) + '|' + str(int(time.time()))


def main():
    client = datastore.Client()

    region_dict = {}

    query = client.query(kind='DsP1RegionCodes')
    for entity in query.fetch():
        key = entity.key
        country_key = key.parent
        if country_key.name not in region_dict:
            region_dict[country_key.name] = dict()
        region_dict[country_key.name][entity['region_code']] = {'id': key.name, 'areas': set()}

    query = client.query(kind='DsP1AreaCodes')
    for entity in query.fetch():
        key = entity.key
        region_key = key.parent
        country_key = region_key.parent
        region = client.get(region_key)

        region_dict[country_key.name][region['region_code']]['areas'].add(entity['area_code'])

    areas = [("US", "zip_code_database.xlsx", "read_excel", 0, 0, 1)]

    for area in areas:
        country_code, area_file, read_method, header, zip_index, state_index = area

        df = getattr(pd, read_method)(area_file, header=header)
        for row in df.iterrows():
            fields = row[1]
            state_code = fields[state_index]
            zip_code = fields[zip_index]
            if type(zip_code) == int:
                zip_code = '{:05d}'.format(zip_code)

            if not (
                    (country_code in region_dict)
                    and
                    (state_code in region_dict[country_code])
            ):
                continue

            if zip_code in region_dict[country_code][state_code]['areas']:
                continue

            print("AREA:", country_code, state_code, zip_code)
            area_key = client.key(
                'DsP1CountryCodes', country_code,
                'DsP1RegionCodes', region_dict[country_code][state_code]['id'],
                'DsP1AreaCodes', generate_area_id(),
            )
            entity = datastore.Entity(key=area_key)
            entity['area_code'] = zip_code
            client.put(entity)


if __name__ == '__main__':
    main()
