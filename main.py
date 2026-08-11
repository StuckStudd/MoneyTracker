import json
import time
import os
from colorama import Style, Fore

# commands 
command_list = ['!help', '!set_money', '!my_purchases', '!my_transactions', '!reset_money', '!balance', '!clear_transactions']

# Opening a JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Creation command
def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# main code 
print(Fore.GREEN + "Welcome to Money Tracker." + Style.RESET_ALL)
time.sleep(1)
clear_console()

if data.get('user', "") == "":
    print(Fore.YELLOW + "Input your name " + Style.RESET_ALL)
    user_name = input('-->> ')
    data['user'] = user_name
    save_data()

while True:
    clear_console()
    print(Fore.GREEN + f"Your current balance : {data.get('money', 0)}" + Style.RESET_ALL)
    print("###########")
    print("Current command : !help !set_money !my_purchases, !my_transactions, !reset_money, !clear_transactions, !exit")
    
    users_commd = input("-->> ").lower().strip()

    if users_commd == command_list[0]:
        clear_console()
        print(Fore.YELLOW + "command !set_money Sets a balance for you that you'll spend, and all transactions will be recorded" + Style.RESET_ALL)
        print(Fore.YELLOW + "command !my_transactions will show you all your transactions" + Style.RESET_ALL)
        print(Fore.YELLOW + "command !my_purchases You can add what you bought, for example what you bought and how much you spent" + Style.RESET_ALL)
        print(Fore.YELLOW + "command !reset_money resets your money" + Style.RESET_ALL)
        time.sleep(6.2)
        continue

    elif users_commd == command_list[1]:
        try: 
            print("Input how much money do you have")
            set_money = float(input("-->> "))
            data['money'] += set_money
            save_data()
        except ValueError:
            print(Fore.RED + " Only nummer!" + Style.RESET_ALL)
            time.sleep(4.3)

    
    elif users_commd == command_list[2]:
        print("Write what you bought")
        bought_item = input("-->> ")

        try:
            spent_money = float(input("Write down how much money you spent: "))
            
            data["transactions"]["acquired"].append(bought_item)
            data["transactions"]["spent"].append(spent_money)
            
     
            data['money'] -= spent_money
            save_data()
            
            print("Saved.")
            time.sleep(1.5)

        except ValueError:
            print(Fore.RED + "Only number" + Style.RESET_ALL)
            time.sleep(4.3)


    elif users_commd == command_list[3]:
        clear_console()
        print(Fore.GREEN + "--- Your transactions ---" + Style.RESET_ALL)
        print(f"Purchased items: {data['transactions']['acquired']}")
        print(f"Spent amounts: {data['transactions']['spent']}")
        input("\nPress Enter to continue...")


    elif users_commd == command_list[4]:
        clear_console()
        confirm = input('Are you sure? y/n -> ').strip().lower()

        if confirm == "y":
            data['money'] = 0
            save_data()
            print("Saved.")
            continue
        
        elif confirm == "n":
            continue
            
 
    elif users_commd == command_list[5]:
        clear_console()
        print(Fore.GREEN + f"Balance : {data['money']}")
        time.sleep(5)
        continue

    elif users_commd == command_list[6]:
        data['transactions']['acquired'].clear()
        data['transactions']['spent'].clear()
        print(Fore.GREEN + "Success!" + Style.RESET_ALL)
        save_data()
        time.sleep(1.2)
        continue
        
    elif users_command == command_list[7]:
        print("See you later..")
        time.sleep(2)
        break
