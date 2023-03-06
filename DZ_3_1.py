import requests

def test_requests():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    return response.json()


my = test_requests()
hero_list = []
hero_dict = {}
for i in my:
    if i['id'] == 1 or i['id'] == 149 or i['id'] == 655:
        hero_dict = {'name': i['name'], 'intelligence': i['powerstats']['intelligence']}
        hero_list.append(hero_dict)
hero_sort_list = sorted(hero_list, key=lambda x: ['intelligence'])

print(hero_sort_list[-1]['name'])