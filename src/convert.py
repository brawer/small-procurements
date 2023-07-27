import csv
import os.path


def read_csv(filename):
    path = os.path.join(os.path.dirname(__file__), 'data', filename)
    with open(path, 'r') as csv_file:
        for row in csv.DictReader(csv_file):
            yield row

    
def read_ch_post():
    for row in read_csv('ch_post_2021.csv'):
        print(row)
        yield row


if __name__ == '__main__':
    for x in read_ch_post():
        print(x)

