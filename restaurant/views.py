from rest_framework.views import APIView
from rest_framework.response import Response
from file_parser.csv_reader import read_csv_file


class TestView(APIView):
    def get(self, request):

        read_csv_file('to_parse_files/small_list.csv')

        return Response({"message": "Hello, World!"})
