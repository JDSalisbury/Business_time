from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from file_parser.csv_reader import read_csv_file
from .models import Restaurant
from .serializers import RestaurantSerializer, RestaurantAndHoursSerializer
from rest_framework.decorators import action
from .time_conversions import convert_query_param_time_to_filter_db_time as convert_time


class UploadCSV(APIView):
    def get(self, request):
        try:
            read_csv_file('to_parse_files/Restaurant.csv')
        except Exception as e:
            return Response({"message": f"An error occurred: {e}"}, status=400)

        return Response({"message": "CSV file uploaded successfully"})


class RestaurantViewset(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantAndHoursSerializer

    @action(detail=False, methods=['get'])
    def open_restaurants(self, request):
        requested_time = request.query_params.get('time', None)
        if not requested_time:
            return Response({"message": "Please provide a time in the following format <Day>@<Time>"}, status=400)

        try:
            day, time = requested_time.split('@')
        except ValueError:
            return Response({"message": "Please provide a time in the following format <Day>@<Time>"}, status=400)

        day = day.capitalize()
        time = time.lower()

        if day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            return Response({"message": "Invalid day provided"}, status=400)
        if len(time.split(':')) != 2:
            print(time.split(':'))
            return Response({"message": "Invalid time format, please provide a time in the following format 1:23pm, 12:34am"}, status=400)
        if time[-2:] not in ['am', 'pm']:
            return Response({"message": "Invalid time format, please provide a time in the following format 1:23pm, 12:34am"}, status=400)

        queryset = Restaurant.objects.filter(
            hour__day__name=day,
            hour__open__lte=convert_time(time),
            hour__close__gt=convert_time(time),
        ).distinct()

        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)
