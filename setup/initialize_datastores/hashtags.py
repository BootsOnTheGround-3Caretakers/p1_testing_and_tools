from __future__ import print_function

import pandas as pd
from google.cloud import datastore


def main():
    client = datastore.Client()

    hashtags = set()

    query = client.query(kind='DsP1HashTags')
    for entity in query.fetch():
        hashtags.add(entity['name'])

    df = pd.read_excel("P1 initial datastore data.xlsx", header=0)
    for row in df.iterrows():
        fields = row[1]
        hashtag = fields[12]

        if not (hashtag and type(hashtag) == str):
            break

        if hashtag in hashtags:
            continue

        print("HASHTAG:", hashtag)
        key = client.key('DsP1HashTags')
        entity = datastore.Entity(key=key)
        entity['name'] = hashtag
        client.put(entity)


if __name__ == '__main__':
    main()
