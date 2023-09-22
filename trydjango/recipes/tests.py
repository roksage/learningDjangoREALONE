from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import RecipeIngredient, Recipe
from .validators import validate_unit_of_measure
from django.core.exceptions import ValidationError


User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')

    def test_user_pw(self):
        checked = self.user_a.check_password("abc123")
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')
        self.recipe_a = Recipe.objects.create(
            name='Grilled Chicken',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='Grilled Chicken Tacos',
            user = self.user_a
        )
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='1/2',
            unit='pound'
        )
        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='1/2',
            unit='pound'
        )

    
    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user = user)
        self.assertEqual(qs.count(), 2) 

    def test_user_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
        self.assertEqual(qs.count(), 2) 

    def test_recipe_ingridientcount(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user = user)
        self.assertEqual(qs.count(), 2) 

    def test_user_two_level_relation_reverse(self):
        user = self.user_a
        recipeingredient_ids = list(user.recipe_set.all().values_list('recipeingredient__id', flat=True))
        qs = RecipeIngredient.objects.filter(id__in=recipeingredient_ids)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation_via_recipes(self):
        user = self.user_a
        ids = user.recipe_set.all().values_list('id', flat = True)
        qs = RecipeIngredient.objects.filter(recipe__id__in=ids)
        self.assertEqual(qs.count(), 2)




    def test_unit_measure_validation_error(self):
        invalid_unit = 'nadaaaa'
        ingredient = RecipeIngredient(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='1/2',
            unit='pound')
         
        ingredient.full_clean()

    

    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_float)
        self.assertIsNotNone(self.recipe_ingredient_b.quantity_as_float)