import requests
import json

class Character(object):
	name = ""
	realm = ""
	level = ""
		
def as_character(data):
	c = Character()
	c.__dict__.update(data)
	return c

char_url = 'https://us.api.blizzard.com/wow/character/darkspear/Saelune?fields=items&locale=en_US&access_token=USSQJJVk6ObbnvwxED3S9qQ4TmmXYpneXk'

response = requests.get(url=char_url)
data = json.loads(response.text)
sdata = json.dumps(data)
#print(json.dumps(data, indent=4, sort_keys=True))

o = json.loads(sdata, object_hook=as_character)
print('\nCharacter Name: {}'.format(o.name))
print('Character Realm: {}'.format(o.realm))
print('Character Level: {}'.format(o.level))
print('Equipped ilvl: {}'.format(o.items.averageItemLevelEquipped))
print('Battlegroup: {}'.format(o.battlegroup))
print('Achievement Points: {}'.format(o.achievementPoints))
print('\nItems:')
print('\tHead: {}, ilvl: {}'.format(o.items.head.name, o.items.head.itemLevel))
print('\tNeck: {}, ilvl: {}'.format(o.items.neck.name, o.items.neck.itemLevel))
print('\tShoulder: {}, ilvl: {}'.format(o.items.shoulder.name, o.items.shoulder.itemLevel))
print('\tBack: {}, ilvl: {}'.format(o.items.back.name, o.items.back.itemLevel))
print('\tChest: {}, ilvl: {}'.format(o.items.chest.name, o.items.chest.itemLevel))
print('\tShirt: {}, ilvl: {}'.format(o.items.shirt.name, o.items.shirt.itemLevel))
print('\tLegs: {}, ilvl: {}'.format(o.items.legs.name, o.items.legs.itemLevel))
print('\tWrists: {}, ilvl: {}'.format(o.items.wrist.name, o.items.wrist.itemLevel))
print('\tHands: {}, ilvl: {}'.format(o.items.hands.name, o.items.hands.itemLevel))
print('\tWaist: {}, ilvl: {}'.format(o.items.waist.name, o.items.waist.itemLevel))
print('\tFeet: {}, ilvl: {}'.format(o.items.feet.name, o.items.feet.itemLevel))
print('\tFinger1: {}, ilvl: {}'.format(o.items.finger1.name, o.items.finger1.itemLevel))
print('\tFinger2: {}, ilvl: {}'.format(o.items.finger2.name, o.items.finger2.itemLevel))
print('\tTrinket1: {}, ilvl: {}'.format(o.items.trinket1.name, o.items.trinket1.itemLevel))
print('\tTrinket2: {}, ilvl: {}'.format(o.items.trinket2.name, o.items.trinket2.itemLevel))
print('\tMain Hand: {}, ilvl: {}'.format(o.items.mainHand.name, o.items.mainHand.itemLevel))
print('\tOff Hand: {}, ilvl: {}'.format(o.items.offHand.name, o.items.offHand.itemLevel))








