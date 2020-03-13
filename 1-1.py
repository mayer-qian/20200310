import requests

url = "https://deckofcardsapi.com/api/deck/he84ehjxswzn/draw/?count=3"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
# print(deck)
#print(aa)

