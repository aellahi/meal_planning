# Reads desired recipes from recipes folder
# and adds them as items in ToDoist Grocery list

import sys
from todoist import TodoistAPI
import pandas as pd

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

# Load ToDoist project

#define token
token='55d2e370c57338fb259642de78bab09867742518'

api = TodoistAPI(token=token)
api.sync()

# Load projects
Projects = api.state['projects']
# grab 'Groceries' project_id
project_id = None
for project in Projects:
    if project['name']=='Groceries':
        project_id = project['id']
    if project['name']=='Inbox':
        inbox = project['id']


# try adding item to inbox
api.items.add('test', **{'project_id':inbox})
api.items.
# Raise warning if no Groceries project found
if project_id:
    print("Found Groceries project!")
else:
    print('Warning! No "Groceries" project found.')

'''
# iterate through summed_ingredients and add to ToDoist grocery list
for row in summed_ingredients.itertuples():
    tup=(row.ingredient, row.amt)
    str_list = [x for x in map(str,tup)]
    to_add = '_'.join(str_list)
    added = api.items.add(to_add, **{'project_id':project_id})
    if added['id']:
       print(f"Successfully added {to_add}.")
    break

api.sync()
'''
