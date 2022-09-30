from django.contrib import admin
from .models import FoodTable, TrainingTable, ColumnTable
# Register your models here.
admin.site.register(FoodTable)
admin.site.register(TrainingTable)
admin.site.register(ColumnTable)
