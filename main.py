import requests, json, methods

def main():
    while True:

        print('******Välkommen!******')
        print('1. Sök efter titel')
        print('2. Sökhistorik')
        print('3. Sök efter ord')
        print('4. Avsluta program')

        user_choice = int(input())
        match user_choice:
            case 1:
                methods.search_title()
            case 2:
                print('nej')
            case 3:
                methods.search_word()
            case 4:
                return
            case _:
                print('ERROR')

main()




