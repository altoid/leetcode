#!/usr/bin/env python

# take an inputfile that looks like this:
#
# +------+------------+-----------+
# | id   | visit_date | people    |
# +------+------------+-----------+
# | 1    | 2017-01-01 | 10        |
# | 2    | 2017-01-02 | 109       |
# | 3    | 2017-01-03 | 150       |
# | 4    | 2017-01-04 | 99        |
# | 5    | 2017-01-05 | 145       |
# | 6    | 2017-01-06 | 1455      |
# | 7    | 2017-01-07 | 199       |
# | 8    | 2017-01-09 | 188       |
# +------+------------+-----------+
#
# and turn it into ddl and instert statements that will create the table.
# output is the ddl/insert statements that can be redirected to a file.

import argparse
import fileinput
from pprint import pprint


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('database')
    parser.add_argument('table')
    parser.add_argument('filename')

    args = parser.parse_args()

    database = args.database
    table = args.table
    filename = args.filename

    fi = fileinput.FileInput(files=(filename,))
    line = fi.readline().strip()
    while not line:
        line = fi.readline().strip()

    # assume line looks like +-------+--------+------+
    # so get the next one, which is the column headers

    line = fi.readline().strip()
    column_names = line.split()
    column_names = list(filter(lambda x: x != '|', column_names))

    # another +-----+ line
    line = fi.readline().strip()

    # now the data
    rows = []
    line = fi.readline().strip()
    while line:
        if line.startswith('+-'):
            break

        data = line.split()
        data = list(filter(lambda x: x != '|', data))
        rows.append(data)
        line = fi.readline().strip()

    ncolumns = len(column_names)

    # transpose the data matrix
    rowsT = [[row[i] for row in rows] for i in range(len(rows[0]))]

    converted_matrix = []
    types = []
    # convert the column values to ints if possible
    for rT in rowsT:
        try:
            converted_row = list(map(int, rT))
            types.append('int')
        except ValueError as v:
            # oops, leave the values alone
            converted_row = rT
            longest = max(converted_row, key=len)
            types.append('varchar(%s)' % len(longest))
        converted_matrix.append(converted_row)

    # transpose it back
    rows = [[row[i] for row in converted_matrix] for i in range(len(converted_matrix[0]))]

    column_names_and_types = list(zip(column_names, types))

    print("use %s;" % database)
    print()
    print("drop table if exists %s;" % table)
    print()
    print("create table %s (" % table)
    i = 0
    while i < len(column_names_and_types) - 1:
        print("%s %s," % (column_names_and_types[i][0], column_names_and_types[i][1]))
        i += 1
    print("%s %s" % (column_names_and_types[i][0], column_names_and_types[i][1]))
    print(") engine=innodb;")
    print()

    format_string = []
    for t in types:
        if t == 'int':
            format_string.append("%s")
        else:
            format_string.append("'%s'")
    format_string = ', '.join(format_string)
    format_string = "(" + format_string + ")"
    print("insert into %s values" % table)
    i = 0
    while i < len(rows) - 1:
        print(format_string % tuple(rows[i]), end=',')
        print()
        i += 1
    print(format_string % tuple(rows[i]))
    print(";")
