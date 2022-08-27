from django.contrib import admin
from .models import Recipe, Measure, FoodItem, Ingredient, Step

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Measure)
admin.site.register(FoodItem)
admin.site.register(Ingredient)
admin.site.register(Step)
