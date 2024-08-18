from django.test import TestCase
from .time_conversions import convert_csv_time_to_db_time, convert_query_param_time_to_filter_db_time

# Create your tests here.
from .csv_to_db import is_day_range, day_range_to_list_of_days, csv_entry_to_restaurant_db
from .models import Restaurant, Day
from file_parser.csv_reader import RestaurantEntry


class TimeConversionTests(TestCase):

    def test_convert_csv_time_to_db_time(self):
        self.assertEqual(convert_csv_time_to_db_time("11 AM"), "11:00")
        self.assertEqual(convert_csv_time_to_db_time("11:30 AM"), "11:30")
        self.assertEqual(convert_csv_time_to_db_time("11 PM"), "23:00")
        self.assertEqual(convert_csv_time_to_db_time("11:30 PM"), "23:30")

    def test_convert_query_param_time_to_filter_db_time(self):
        self.assertEqual(
            convert_query_param_time_to_filter_db_time("11:30AM"), "11:30:00")
        self.assertEqual(convert_query_param_time_to_filter_db_time(
            "11:30PM"), "23:30:00")


class TestCSVToDB(TestCase):

    def test_is_day_range(self):
        arrange_date_range = "Mon-Thu"
        arragne_date = "Mon"

        undertest_date_range = is_day_range(arrange_date_range)
        undertest_date = is_day_range(arragne_date)

        self.assertTrue(undertest_date_range)
        self.assertFalse(undertest_date)

    def test_day_rang_to_list_of_days(self):
        arrange_date_range = "Mon-Thu"

        undertest_date_range = day_range_to_list_of_days(arrange_date_range)

        self.assertEqual(undertest_date_range, ["Mon", "Tues", "Wed", "Thu"])

    def test_csv_to_restaurant_db(self):
        arrange_restaurant_entry = RestaurantEntry(name="Test Restaurant",
                                                   hours=["Mon 11 AM - 8 PM", "Tues 11 AM - 8 PM", "Wed 11 AM - 8 PM"])

        csv_entry_to_restaurant_db(arrange_restaurant_entry)

        restaurant = Restaurant.objects.get(name="Test Restaurant")
        self.assertEqual(restaurant.hour_set.count(), 3)
        self.assertEqual(restaurant.hour_set.filter(
            day__name="Monday").count(), 1)
        self.assertEqual(restaurant.hour_set.filter(
            day__name="Tuesday").count(), 1)

    def test_csv_to_restaurant_db_with_day_range(self):
        arrange_restaurant_entry = RestaurantEntry(name="Test RestaurantRange",
                                                   hours=["Mon-Wed 11 AM - 8 PM"])

        csv_entry_to_restaurant_db(arrange_restaurant_entry)
        restaurant = Restaurant.objects.get(name="Test RestaurantRange")

        self.assertEqual(restaurant.hour_set.count(), 3)
        self.assertEqual(restaurant.hour_set.filter(
            day__name="Monday").count(), 1)
        self.assertEqual(restaurant.hour_set.filter(
            day__name="Tuesday").count(), 1)
