from django.db import models
from django.utils.translation import gettext_lazy as _

# note: change model to use ForeignKey
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_image = models.ImageField()
    prep_time = models.DurationField()
    ingredients = models.TextField()
    instructions = models.TextField()

    class TypeOfFood(models.TextChoices):
        APPETIZER = 'AP', _('Appetizer')
        ENTREE = 'EN', _('Entree')
        DESSERT = 'DS', _('Dessert')
        DRINK = 'DR', _('Drink')
        SNACK = 'SN', _('Snack')

    type_of_food = models.CharField(
        max_length=2,
        choices=TypeOfFood.choices,
        default=TypeOfFood.ENTREE,
    )

    class Availability(models.TextChoices):
        STAPLE = 'ST', _('Staple')
        SPECIAL = 'SP', _('Special')

    availability = models.CharField(
        max_length=2,
        choices=Availability.choices,
        default=Availability.STAPLE,
    )
    
    def is_staple(self):
        return self.availability is self.Availability.STAPLE
    
        
