from datetime import datetime


def convert_csv_time_to_db_time(time_str):
    # ChatGPTed
    # Parse the time string to a datetime object
    dt = datetime.strptime(time_str, "%I %p") if len(
        time_str.split(':')) == 1 else datetime.strptime(time_str, "%I:%M %p")

    # Convert to 24-hour format and return as HH:MM
    return dt.strftime("%H:%M")


def convert_query_param_time_to_filter_db_time(time_str):
    dt = datetime.strptime(time_str, '%I:%M%p')
    return dt.strftime("%H:%M:%S")
