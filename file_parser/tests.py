from django.test import TestCase
from file_parser.csv_reader import days_hour_range_break, compound_hour_break, break_hours_on_slash_and_strip

# Create your tests here.


class TestFileParser(TestCase):

    def test_days_hours_range_break(self):
        arrange_hours = "Mon-Thu 11:30 am - 10 pm"

        undertest_days, undertest_time_range = days_hour_range_break(
            arrange_hours)
        self.assertEqual(undertest_days, "Mon-Thu")
        self.assertEqual(undertest_time_range, "11:30 am - 10 pm")

    def test_coumpound_hour_break(self):
        arrange_hours = "Mon-Thu, Fri-Sat 11:30 am - 10 pm"
        undertest = compound_hour_break(arrange_hours)
        self.assertEqual(
            undertest, ["Mon-Thu 11:30 am - 10 pm", "Fri-Sat 11:30 am - 10 pm"])

    def test_break_hours_on_slash_and_strip(self):
        arrange_hours = ["Mon-Fri, Sat 11 am - 12 pm  / Sun 11 am - 10 pm"]
        undertest = break_hours_on_slash_and_strip(arrange_hours)
        self.assertEqual(
            undertest, ["Mon-Fri, Sat 11 am - 12 pm", "Sun 11 am - 10 pm"])
