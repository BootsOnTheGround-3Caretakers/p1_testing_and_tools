from __future__ import print_function

import pandas as pd
from google.cloud import datastore


def main():
    client = datastore.Client()

    need_names = set()

    query = client.query(kind='DsP1Needs')
    for entity in query.fetch():
        need_names.add(entity['need_name'])

    df = pd.read_excel("P1 initial datastore data.xlsx", header=0)
    for row in df.iterrows():
        fields = row[1]
        need_name = fields[10]

        if not (need_name and type(need_name) == str):
            break

        if need_name in need_names:
            continue

        print("NEED NAME:", need_name)
        key = client.key('DsP1Needs')
        entity = datastore.Entity(key=key)
        entity['need_name'] = need_name
        client.put(entity)


if __name__ == '__main__':
    main()
