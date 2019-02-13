import requests
import json


char_url = 'https://us.api.blizzard.com/wow/character/darkspear/Saelune?fields=items&locale=en_US&access_token=USSQJJVk6ObbnvwxED3S9qQ4TmmXYpneXk'
item_url = 'https://us.api.blizzard.com/wow/item/{}?locale=en_US&access_token=USSQJJVk6ObbnvwxED3S9qQ4TmmXYpneXk'

response = requests.get(url=char_url)
data = json.loads(response.text)
#print(json.dumps(data, indent=4, sort_keys=True))
items = data['items']
char_items = data['items']
char_dict = {}

char_dict['Character Name'] = data['name']
char_dict['Character Realm'] = data['realm']
char_dict['Character Level'] = data['level']

for key in items.keys():
	if "head" in key:
		char_dict['Head'] = items[key]['id']
		char_dict['Head ilvl'] = items[key]['itemLevel']
	elif "neck" in key:
		char_dict['Neck'] = items[key]['id']
		char_dict['Neck ilvl'] = items[key]['itemLevel']
	elif "shoulder" in key:
		char_dict['Shoulder'] = items[key]['id']
		char_dict['Shoulder ilvl'] = items[key]['itemLevel']
	elif "back" in key:
		char_dict['Back'] = items[key]['id']
		char_dict['Back ilvl'] = items[key]['itemLevel']
	elif "chest" in key:
		char_dict['Chest'] = items[key]['id']
		char_dict['Chest ilvl'] = items[key]['itemLevel']
	elif "wrist" in key:
		char_dict['Wrist'] = items[key]['id']
		char_dict['Wrist ilvl'] = items[key]['itemLevel']
	elif "hands" in key:
		char_dict['Hands'] = items[key]['id']
		char_dict['Hands ilvl'] = items[key]['itemLevel']
	elif "waist" in key:
		char_dict['Waist'] = items[key]['id']
		char_dict['Waist ilvl'] = items[key]['itemLevel']
	elif "legs" in key:
		char_dict['Legs'] = items[key]['id']
		char_dict['Legs ilvl'] = items[key]['itemLevel']
	elif "feet" in key:
		char_dict['Feet'] = items[key]['id']
		char_dict['Feet ilvl'] = items[key]['itemLevel']
	elif "finger1" in key:
		char_dict['Finger1'] = items[key]['id']
		char_dict['Finger1 ilvl'] = items[key]['itemLevel']
	elif "finger2" in key:
		char_dict['Finger2'] = items[key]['id']
		char_dict['Finger2 ilvl'] = items[key]['itemLevel']
	elif "trinket1" in key:
		char_dict['Trinket1'] = items[key]['id']
		char_dict['Trinket1 ilvl'] = items[key]['itemLevel']
	elif "trinket2" in key:
		char_dict['Trinket2'] = items[key]['id']
		char_dict['Trinket2 ilvl'] = items[key]['itemLevel']
	elif "mainHand" in key:
		char_dict['Main Hand'] = items[key]['id']
		char_dict['Main Hand ilvl'] = items[key]['itemLevel']
	elif "offHand" in key:
		char_dict['Off Hand'] = items[key]['id']
		char_dict['Off Hand ilvl'] = items[key]['itemLevel']


for key in char_dict.keys():
	if 'ilvl' not in key and "Character" not in key:
		item_response = requests.get(item_url.format(char_dict[key]))
		item_data = json.loads(item_response.text)
		char_dict[key] = item_data['name']

for (k, v) in char_dict.items():
	print('{}: {}'.format(k, v))






