print("""
██████╗░██╗░░░██╗  ██████╗░░█████╗░███╗░░██╗██╗░░██╗  ░███████╗
██╔══██╗██║░░░██║  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝  ██╔██╔══╝
██████╦╝██║░░░██║  ██████╦╝███████║██╔██╗██║█████═╝░  ╚██████╗░
██╔══██╗██║░░░██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗░  ░╚═██╔██╗
██████╦╝╚██████╔╝  ██████╦╝██║░░██║██║░╚███║██║░╚██╗  ███████╔╝
╚═════╝░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚══════╝░
""")

import os, sys
import time

def return_to_main():
    time.sleep(1)
    import main

def resource_path(relative_path): 
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

try:
    path = resource_path("database/account.txt")
    with open(path, "r") as file:
        account = file.read()
        for line in account:
            first, last, birth, cash, accId = account.split(" ", 4)
            
        print(f'{"Account Information":^62}')
        print(f'{"Name: "+first + " " + last:^62}')
        print(f'{"Birthdate: "+birth:^62}')
        print(f'{"Balance: ฿"+ cash +" - Account ID : "+ accId:^62}')

except FileNotFoundError:
    print("Account not found. Returning to main menu.")
    return_to_main()

input("\nEnter to return to main menu...")
import main