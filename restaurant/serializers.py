from rest_framework import serializers
from .models import Restaurant, Hour
from django.db.models import Case, When, Value, IntegerField


class HourSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField()

    class Meta:
        model = Hour
        fields = ['day', 'open', 'close']


class HourSerializerForOpenStatus(serializers.ModelSerializer):
    hours = serializers.SerializerMethodField()

    class Meta:
        model = Hour
        fields = ['hours']

    def get_hours(self, obj):
        return f'{obj.day}: {obj.open} - {obj.close}'


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['name']


class RestaurantAndHoursSerializer(serializers.ModelSerializer):
    # these were unordered. had to manual order with some sudo sql logic in the order_by
    # hours = HourSerializer(many=True, read_only=True, source='hour_set')

    hours = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'hours'
        ]

    def get_hours(self, obj):
        hours = obj.hour_set.all().order_by(
            Case(
                When(day__name='Monday', then=Value(1)),
                When(day__name='Tuesday', then=Value(2)),
                When(day__name='Wednesday', then=Value(3)),
                When(day__name='Thursday', then=Value(4)),
                When(day__name='Friday', then=Value(5)),
                When(day__name='Saturday', then=Value(6)),
                When(day__name='Sunday', then=Value(7)),
                output_field=IntegerField(),
            )
        )
        return HourSerializer(hours, many=True).data
