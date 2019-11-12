# Reads desired recipes from recipes folder
# and adds them as items in ToDoist Grocery list

import sys
from pytodoist import todoist
import pandas as pd
import json

# Load recipe info
# List recipes to create grocery list from:
files = input("Enter comma separated list of recipe files: ")
recipe_list = files.split(',')

recipe_dfs = [pd.read_csv(File) for File in recipe_list]

# combine all ingredients
all_ingredients = pd.concat(recipe_dfs)
all_ingredients.sort_values(by='ingredient', inplace=True)
summed_ingredients = all_ingredients.groupby(['ingredient', 'unit']).sum()
summed_ingredients.reset_index(inplace=True)

# load ToDoist user and password
with open('todoist_login.json','r') as json_file:
    user_credentials = json.load(json_file)

# login to Todoist
user = todoist.login(user_credentials['user'], user_credentials['password'])

# Load Groceries project
groceries = user.get_project('Groceries')

# iterate through summed_ingredients and add to Groceries
for row in summed_ingredients.itertuples():
    tup=(row.ingredient, row.amt)
    str_list = [x for x in map(str,tup)]
    to_add = ' '.join(str_list)
    added = groceries.add_task(to_add)
    if added.content:
       print(f"Successfully added {to_add}.")
