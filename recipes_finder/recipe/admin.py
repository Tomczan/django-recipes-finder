from django.contrib import admin
from .models import Recipe, Ingredient, IngredientType, RecipeIngredients

# Register your models here.


class RecipeIngredientsInLine(admin.TabularInline):
    model = RecipeIngredients
    extra = 1


@admin.register(IngredientType)
class IngredientTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientsInLine,)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientsInLine,)
