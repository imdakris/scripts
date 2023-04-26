#!/bin/python3
import schedule
import requests

def greeting():
    todos_dict = {
        '08:00': 'Drink coffee',
        '09:00': 'Drink coffee',
        '10:00': 'Drink coffee',
        '11:00': 'Drink coffee'
    }
    print("Day's tasks")
    for k, v, in todos_dict.items():
        print(f'{k} - {v}')
        
    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"
    print(btc_price)

def main():
    # greeting()
    schedule.every().day.at('11:44').do(greeting)
    schedule.every().day.thursday.do(greeting)
    schedule.every().friday.at('11:41').do(greeting)
    
    while True:
        schedule.run_pending()
        
        
if __name__ == '__main__':
    main()