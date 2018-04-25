#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Glottolog-datasette serves a Datasette REST api for Glottolog langoid info.

1. load the most recent glottolog database
2. extracts pertinent information
3. output into SQLite database
4. prepare datasette with that database
5. serve
"""

# Imports
import csv
import sqlite3
from pathlib import Path

createStmt = '''
CREATE TABLE languoid (
    "id" TEXT PRIMARY KEY,
    "label" TEXT,
    "type" TEXT,
    "status" TEXT,

    "parent" TEXT,
    "family" TEXT,

    "latitude" REAL,
    "longitude" REAL,
    "iso639P3code" TEXT,

	"child_family_count" INTEGER,
    "child_language_count" INTEGER,
    "child_dialect_count" INTEGER,
        
    FOREIGN KEY (family) REFERENCES languoid(id),
    FOREIGN KEY (parent) REFERENCES languoid(id)
);
'''

insertStmt = '''
INSERT INTO languoid VALUES (?,?,?,?,?,?,?,?,?,?,?,?);
'''


def main():
    conn = sqlite3.connect('glottolog.db')
    c = conn.cursor()
    c.execute(createStmt)

    #
    with open(Path(__file__).parent / 'data' / 'languoid.csv', newline='') as source:
        langreader = csv.reader(source, delimiter=',', quotechar='"')

        next(langreader, None)  # skip the first row, those are headers

        for row in langreader:
            # shuffle around the values of the origin csv and the target insert statement
            id_, family_id, parent_id, name, bookkeeping, level, status, latitude, longitude, iso639P3code, description, markup_description, child_family_count, child_language_count, child_dialect_count, country_ids = row
            data = (id_, name, level, status, parent_id, family_id, latitude, longitude,
                    iso639P3code, child_family_count, child_language_count, child_dialect_count, )
            c.execute(insertStmt, data)

    try:
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print('Changes could not be commited to the database.')
        print(e)
        exit(100)


if __name__ == '__main__':
    main()
