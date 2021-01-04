import requests 

from bs4 import BeautifulSoup


response = requests.get('https://cookpad.com/kondate/categories/6')
#print(response)
#print(response.text)

data = BeautifulSoup(response.text, 'html.parser')

recipe_class_data = data.find(class_="kondate_title")

recipe_title = recipe_class_data.a.string

recipe_url = recipe_class_data.a['href']

#print(recipe_class_data)
#print(recipe_title)
#print(recipe_url)

cookpad_url = 'https://cookpad.com/'

recipe = cookpad_url+recipe_url

print(recipe)

