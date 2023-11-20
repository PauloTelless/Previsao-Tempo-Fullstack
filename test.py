import requests
import pprint
cidade = 'Aracaju'
API_Key = 'e1d46f324e963f3d1654a81751c807cf'
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_Key}&lang=pt_br'
r = requests.get(link).json()
pprint.pprint(r['name'])
    