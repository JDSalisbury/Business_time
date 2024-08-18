from django.contrib import admin

# Register your models here.


from .models import Restaurant, Day, Hour


admin.site.register(Restaurant)
admin.site.register(Day)
admin.site.register(Hour)
