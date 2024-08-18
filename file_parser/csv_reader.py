import csv
from dataclasses import dataclass


@dataclass
class RestaurantEntry:
    name: str
    hours: list

    def __str__(self):
        return f"{self.name}, hours={self.hours}"


def break_hours_on_slash_and_strip(hours):
    # also flattens the list since split returns a list
    return [item.strip() for hour in hours for item in hour.split('/')]


def compound_hour_break(hours):
    # Given a list of hours 'Tues-Fri, Sun 11:30 am - 10 pm', 'Sat 5:30 pm - 11 pm', break on ", " and the output should be something like: ['Tues-Fri 11:30 am - 10:00 pm', 'Sun 11:30 am - 10:00 pm', 'Sat 5:30 pm - 11 pm']
    pass


def hour_parser(hours):
    split_hours = break_hours_on_slash_and_strip(hours)
    return split_hours


def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(file)

        restaurants = []

        for row in reader:
            restaurant_name = row[0]
            hours = row[1:]
            parsed_hours = hour_parser(hours)
            restaurant_entry = RestaurantEntry(restaurant_name, parsed_hours)

            restaurants.append(restaurant_entry)
            print(restaurant_entry)

        return restaurants
