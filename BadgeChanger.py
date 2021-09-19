import requests

token = '' # Your Discord token.
url = 'https://discord.com/api/v6/hypesquad/online'

def rate_limited():
    print('> Status: Error   | Rate limited\n')

def invalid_token():
    print('> Status: Error   | Invalid Discord token\n')

def badges():
    while True:
        option = str(input('[1] Hypesquad Bravery\n[2] Hypesquad Brilliance\n[3] Hypesquad Balance\n\n> Select a Discord Badge: '))

        if option in ['1', 'Hypesquad Bravery', 'House of Bravery', 'Bravery']:
            house_of_bravery = requests.post(url, json = {'house_id': '1'}, headers = {'authorization': token})
            if house_of_bravery.status_code == 204:
                print('> Status: Success | Type: Hypesquad Bravery\n')
            elif house_of_bravery.status_code == 429:
                rate_limited()
            elif house_of_bravery.status_code == 401:
                invalid_token()
                break
            else:
                print('%s\n' % (house_of_bravery.text))

        elif option in ['2', 'Hypesquad Brilliance', 'House of Brilliance', 'Brilliance']:
            house_of_brilliance = requests.post(url, json = {'house_id': '2'}, headers = {'authorization': token})
            if house_of_brilliance.status_code == 204:
                print('> Status: Success | Type: Hypesquad Brilliance\n')
            elif house_of_brilliance.status_code == 429:
                rate_limited()
            elif house_of_brilliance.status_code == 401:
                invalid_token()
                break
            else:
                print('%s\n' % (house_of_brilliance.text))

        elif option in ['3', 'Hypesquad Balance', 'House of Balance', 'Balance']:
            house_of_balance = requests.post(url, json = {'house_id': '3'}, headers = {'authorization': token})
            if house_of_balance.status_code == 204:
                print('> Status: Success | Type: Hypesquad Balance\n')
            elif house_of_balance.status_code == 429:
                rate_limited()
            elif house_of_balance.status_code == 401:
                invalid_token()
                break
            else:
                print('%s\n' % (house_of_balance.text))

        else:
            print('> Status: Error   | Invalid option\n')

while True:
    badges()
    token = str(input('Discord token: '))
