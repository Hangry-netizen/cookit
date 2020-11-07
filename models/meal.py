from models.base_model import BaseModel
import peewee as pw
from playhouse.postgres_ext import *

class Meal(BaseModel):
    name = pw.CharField(unique=True)
    ingredients = JSONField()
    prep_time = pw.CharField()
    cookware = JSONField()
    url = pw.TextField()

    def validate(self):
        duplicate_meal = Meal.get_or_none(Meal.name == self.name)
        print("Meal validation in process")

        if duplicate_meal and self.id != duplicate_meal.id:
            self.errors.append("There is an existing meal with this name!")