from django.contrib import admin
from recipes.models import Recipe, Measure, FoodItem, Ingredient, Step
from tags.models import Tag

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Measure)
admin.site.register(FoodItem)
admin.site.register(Ingredient)
admin.site.register(Step)

admin.site.register(Tag)
