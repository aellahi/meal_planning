# Objects and tools for loading and manipulating recipes
import pandas as pd
import os

class Recipe():
    """
    Recipe object
    """
    def __init__(self):
        self.name = " "

    def parse_name(self, recipe_csv):

        """Returns base recipe_csv name from full filepath.
        e.g, 'recipe_files/cornbread.csv' returns 'cornbread'."""

        csv = os.path.basename(recipe_csv)

        return csv.split(".")[0]

    # TODO: Find some way to specify number of servings in recipe_csv! 
    def add_ingredients(self, recipe_csv):

        """Returns a dictionary keyed by ingredient,
        value equal to a tuple of amount and unit."""

        # set default recipe name to name of csv
        self.name = self.parse_name(recipe_csv)

        self.ingredients = {}
        recipe_df = pd.read_csv(recipe_csv)
        for n, row in recipe_df.iterrows():
            self.ingredients[row.ingredient] = (row.amt, row.unit)

    def replace_ingredient(self, current_ingredient, replacement_ingredient):

        """Replaces an existing ingredient with replacement_ingredient in
        'ingredients' attribute. Calling this method will DELETE the current_ingredient
        from 'ingredients'.

        Arguments:
            -current_ingredient (str): current ingredient name
            -replacement_ingredient (tuple): tuple of ingredient, amount, and unit.

        Returns:
            None

        Raises:
            Exception - if current_ingredient and replacement_ingredient are the same
            Exception - if either 'ingredients' is empty (i.e., the 'add_ingredients' method
            has not been called) or the current_ingredient is not in 'ingredients'
        """
