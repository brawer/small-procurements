import csv
import os.path


SOURCES = {
    'post_ch': (
        'Die Schweizerische Post AG',
        'Wankdorfallee 4',
        '3030', 'Bern',
        'CHE-109.030.864'),
    'wsl_ch': (
        'Eidgenössische Forschungsanstalt für Wald, Schnee und Landschaft',
        'Zürcherstrasse 111',
        '8903', 'Birmensdorf ZH',
        'CHE-116.133.452'),
}


def read_csv(filename):
    path = os.path.join(os.path.dirname(__file__), 'data', filename)
    with open(path, 'r') as csv_file:
        for row in csv.DictReader(csv_file):
            yield row


def read_all():
    for key in SOURCES.keys():
        for row in read_csv(f'{key}_2021.csv'):
            yield row


if __name__ == '__main__':
    for x in read_all():
        print(x)

