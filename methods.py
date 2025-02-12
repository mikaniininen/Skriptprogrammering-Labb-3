import requests, json
import os
import requirements
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('API_KEY')
json_file = 'file_str.json'


def search_title():

    print('För att återgå till meny, skriv "return"')
    user_title = input('Skriv din titel: ')
    print('')
    if user_title == 'return':
        return
    url = 'https://omdbapi.com/?apikey=' + api_key + '&t=' + user_title
    fetch_url_json(url)
    add_history(user_title)

def add_history(user_title):
    with open('search_json.json', 'w', encoding='utf-8') as fpointer:
        wdata = json.dumps(user_title)
        fpointer.write(wdata)
    print_json(json_file)

def fetch_url_json(url):
    response = requests.get(url)
    data = response.json()
    if data.get("Response") == "False":
        print("Din sökning fick inga resultat.")

    with open('file_str.json', 'w', encoding='utf-8') as fpointer:
        wdata = json.dumps(data, indent=4)
        fpointer.write(wdata)

   # if response.status_code != 200:
    #    print('Anslutningen misslyckades')



def print_json(json_file):
    try:
        with open(json_file, 'r', encoding = 'utf-8-sig') as jsonf:
            info_dict = json.load(jsonf)

        keys_to_extract = ['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors']
        filtered_data = {key:info_dict[key] for key in keys_to_extract if key in info_dict}

        with open(json_file, 'w', encoding='utf-8-sig') as jsonf:
            json.dump(filtered_data, jsonf)
            output = json.dumps(filtered_data, indent=4, ensure_ascii=False)
        print(output)


    except FileNotFoundError:
        print('\nERROR: Filen finns inte\n')


#def print_history():



def search_word():
    print('För att återgå till meny, skriv "return"')
    user_word = input('Skriv ditt sökord: ')
    print('')
    if user_word == 'return':
        return
    url = 'https://omdbapi.com/?apikey=' + api_key + '&s=' + user_word
    fetch_url_json(url)
    with open(json_file, 'r', encoding='utf-8') as jsonf:
        results = json.load(jsonf)

    if "Search" not in results:
        print("Inga resultat.")
        return

    keys_to_extract = ['Title', 'Year']
    filtered_data = [{key: movie[key] for key in keys_to_extract if key in movie} for movie in results['Search']]

    with open(json_file, 'w', encoding='utf-8-sig') as jsonf:
        json.dump(filtered_data, jsonf)
    output = json.dumps(filtered_data, indent=4, ensure_ascii=False)
    print(output)









#fetch_url_json(url)


