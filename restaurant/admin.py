from django.contrib import admin
from .models import Restaurant, Day, Hour


class HourAdmin(admin.ModelAdmin):
    search_fields = ['restaurant__name', 'open', 'close']


admin.site.register(Restaurant)
admin.site.register(Day)
admin.site.register(Hour, HourAdmin)
