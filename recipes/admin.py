from django.contrib import admin

from recipes.models import Recipe

from recipes.models import Measure

admin.site.register(Recipe)
# Register your models here.
admin.site.register(Measure)
