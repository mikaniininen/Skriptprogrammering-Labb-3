import requests, json



api_key = 'cc26ded9'



def search_title():
    user_title = input('Skriv din titel: ')
    url = 'https://omdbapi.com/?apikey=' + api_key + '&t=' + user_title
    fetch_url_json(url)
    #search_history.append(user_title)
    with open('search_json.json', 'w', encoding='utf-8') as fpointer:
        wdata = json.dumps(user_title)
        fpointer.write(user_title)

def fetch_url_json(url):
    response = requests.get(url)
    data = response.json()
    with open('file_str.json', 'w', encoding='utf-8') as fpointer:
        wdata = json.dumps(data)
        fpointer.write(wdata)

#fetch_url_json(url)

search_title()
