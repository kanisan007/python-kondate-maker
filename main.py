import requests 

from bs4 import BeautifulSoup

import random

response = requests.get('https://cookpad.com/kondate/categories/6')
#print(response)
#print(response.text)

data = BeautifulSoup(response.text, 'html.parser')

recipe_class_data = data.find_all(class_="kondate_title")

recipe_name_list = []
recipe_url_list = []

for i in range(8):
    recipe_title = recipe_class_data[i].a.string

    recipe_url = recipe_class_data[i].a['href']

    #print(recipe_class_data)
    #print(recipe_title)
    #print(recipe_url)

    cookpad_url = 'https://cookpad.com/'

    recipe_name_list.append(recipe_title)
    recipe_url_list.append(cookpad_url+recipe_url)

today_recipe_number = random.randint(0,7)

print(recipe_name_list[today_recipe_number])
print(recipe_url_list[today_recipe_number])