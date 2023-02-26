import random

from bs4 import BeautifulSoup
import requests

COOKPAD_URL = 'https://cookpad.com'

response = requests.get(COOKPAD_URL + '/kondate/categories/6')
data = BeautifulSoup(response.text, 'html.parser')
recipe_elements = data.find_all(class_='kondate_title')

recipes = []

for element in recipe_elements:
    recipe_title = element.a.string
    recipe_path = element.a['href']

    recipes.append({
        'title': recipe_title,
        'url': COOKPAD_URL + recipe_path,
    })

recipe = recipes[random.randint(0, len(recipe_elements) - 1)]

print(recipe['title'])
print(recipe['url'])
