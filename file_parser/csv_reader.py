import csv
from dataclasses import dataclass


@dataclass
class RestaurantEntry:
    name: str
    hours: list

    def __str__(self):
        return f"{self.name}, hours={self.hours}"


def break_hours_on_slash_and_strip(hours):
    """
    Breaks down the hours string on the slash and strips the whitespace
    input: "11:30 am - 10 pm / 11:30 am - 10 pm"
    output: ["11:30 am - 10 pm", "11:30 am - 10 pm"]
    """

    # also flattens the list since split returns a list
    return [item.strip() for hour in hours for item in hour.split('/')]


def days_hour_range_break(hours):
    """
    Breaks down the days and time range from the hours string
    input: "Mon-Thu 11:30 am - 10 pm"
    output: "Mon-Thu", "11:30 am - 10 pm"
    """
    split_hours = hours.split(' ')
    days = split_hours[0]
    time_range = ' '.join(split_hours[1:])
    return days, time_range


def compound_hour_break(hours) -> list:
    """
    Breaks down the compound hours into individual hours
    input: "Mon-Thu, Fri-Sat 11:30 am - 10 pm"
    output: ["Mon-Thu 11:30 am - 10 pm", "Fri-Sat 11:30 am - 10 pm"]
    """
    split_hours = [part.strip() for part in hours.split(',')]
    day_range_on_end, time = days_hour_range_break(split_hours[-1])
    days = split_hours[:-1]
    days.append(day_range_on_end)

    parsed = []
    for day in days:
        parsed.append(f"{day} {time}")

    return parsed


def hour_parser(hours):
    split_hours = break_hours_on_slash_and_strip(hours)
    for hour in split_hours:
        if ',' in hour:
            parsed_compunded_hours = compound_hour_break(hour)
            split_hours.remove(hour)
            split_hours.extend(parsed_compunded_hours)

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

        print("_" * 50)
        for rest in restaurants:
            print(rest)

        return restaurants
