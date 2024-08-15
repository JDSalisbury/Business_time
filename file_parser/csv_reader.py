import csv
from dataclasses import dataclass


@dataclass
class RestaurantEntry:
    name: str
    hours: list

    def __str__(self):
        return f"{self.name}, hours={self.hours}"


def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(file)

        for row in reader:
            restaurant_entry = RestaurantEntry(name=row[0], hours=row[1:])
            print(restaurant_entry)
