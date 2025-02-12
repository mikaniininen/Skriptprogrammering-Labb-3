import requests, json, methods

def main():
    user_choice = int(input())
    match user_choice:
        case 1:
            methods.search_title()
        case 2:
            print('nej')
        case 3:
            methods.search_word()
        case _:
            print('ERROR')

main()




