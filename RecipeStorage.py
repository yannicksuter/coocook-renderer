import Recipe
from pymongo import MongoClient

DATABASE_NAME = 'cookoob-dev'

class RecipeStorage(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[DATABASE_NAME]
        self.recipes = self.db.recipes

    def load(self, id):
        recipe = self.recipes.find_one({'_id': id})
        return recipe

    def store(self, recipe):
        result = self.recipes.update({'_id': recipe._id}, recipe.__dict__, True)
        # print('Recipe inserted: {0}'.format(result.inserted_id))
        # print(result)