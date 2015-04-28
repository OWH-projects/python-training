import requests
r = requests.get('http://api.census.gov/data/2010/sf1')

if r.status_code == 200:
    print r.json()