from os import system
import requests
from sys import argv

def clear_screen():
    _ = system('cls')

clear_screen()

input_Pokemon = argv[1]

def main():
    Pokemon_name = argv[1]
    Pokemon_info = get_pokemon_info(Pokemon_name)
    if Pokemon_info:
        pb_strings = get_title_and_text(Pokemon_info)
        pb_url = post_to_pastebin(pb_strings[0], pb_strings[1])
        return(pb_url)
        
def post_to_pastebin(title, body_text):

    print("Posting to pastebin...", end='')

    pastebin_params = {
        'Api_Dev_Key': "DUELWx3afIG04vOY4f531kRhgd_f1O1w",
        'Api_Option': 'paste',
        'Api_Paste_Code': body_text,
        'Api_Paste_Name': title,
    }
    response = requests.post('https://pastebin.com/api/api_post.php', data = pastebin_params)

    if response.status_code == 200:
        print('success')
        return response.text
    else:
        print('failed. Response code:', response.status_code)
        return response.status_code

def get_pokemon_info(Pokemon_name):
    print("Getting Pokemon information...", end='')
    response = requests.get('https://pokeapi.co/api/v2/pokemon/mew' + str(Pokemon_name))

    if response.status_code == 200:
        print('success')
        return response.json()
    else:
        print('failed. Response code:', response.status_code)
        return

def get_title_and_text(Pokemon_info):

    body_text = ""

    title = Pokemon_info['name'] + "'s stats"
    print(title)
    for i in Pokemon_info['abilities']:
        print(i['ability']['name'])

main()