from .models import Restaurant, Hour, Day
from datetime import datetime


def convert_time(time_str):
    # ChatGPTed
    # Parse the time string to a datetime object
    dt = datetime.strptime(time_str, "%I %p") if len(
        time_str.split(':')) == 1 else datetime.strptime(time_str, "%I:%M %p")

    # Convert to 24-hour format and return as HH:MM
    return dt.strftime("%H:%M")


def is_day_range(day_range):
    return '-' in day_range


def day_range_to_list_of_days(day_range):
    """
    Takes a string of days in the format "Mon-Thu" and returns a list of days
    input: "Mon-Thu"
    output: ["Mon", "Tues", "Wed", "Thu"]
    """
    days = ["Mon", "Tues", "Wed", "Thu",
            "Fri", "Sat", "Sun"]
    start, end = day_range.split('-')
    start_index = days.index(start)
    end_index = days.index(end)
    return days[start_index:end_index + 1]


def csv_entry_to_restaurant_db(restaurant_entry):
    restaurant, _ = Restaurant.objects.get_or_create(
        name=restaurant_entry.name)

    for hour in restaurant_entry.hours:
        print(hour)
        day, time_range = hour.split(' ', 1)
        start, end = time_range.split(' - ')

        if is_day_range(day):
            days = day_range_to_list_of_days(day)
            for day in days:
                day_obj = Day.objects.get(abbr=day)
                Hour.objects.update_or_create(restaurant=restaurant,
                                              day=day_obj, open=convert_time(start), close=convert_time(end))
        else:
            day_obj = Day.objects.get(abbr=day)
            Hour.objects.update_or_create(restaurant=restaurant,
                                          day=day_obj, open=convert_time(start), close=convert_time(end))
