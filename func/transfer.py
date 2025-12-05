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
    targeting = int(input("Enter destination account ID: "))
    amount = float(input("Enter amount to transfer: "))
    accept = input(f"Make sure the account ID -> {targeting} and amount -> {amount} are correct ( y , n )")
    if accept.lower() != 'y':
        print("Transfer cancelled. Returning to main menu...")
        return_to_main()
    elif accept.lower() == 'y':
        try:
            account_database = resource_path("database/account.txt")
            users_database = resource_path("database/users.txt")
            target_index = None
            target_first = target_last = target_birth = None
            target_cash = 0.0

            with open(users_database, "r", encoding="UTF-8") as file:
                users_memory = file.readlines()
                for i, line in enumerate(users_memory):
                    first, last, birth, cash, accID = line.split(" ", 4)
                    if accID.strip() == str(targeting):
                        target_index = i
                        target_first = first
                        target_last = last
                        target_birth = birth
                        target_cash = float(cash)
                        break
                if target_index is None:
                    print("Destination account not found. Returning to main menu...")
                    return_to_main()
            with open(account_database, "r", encoding="UTF-8") as file:
                line = file.readline().strip()
                first, last, birth, cash, accID = line.split(" ", 4)
                user_cash = float(cash)
                if amount > user_cash:
                    print("Insufficient funds. Returning to main menu...")
                    return_to_main()
                user_cash -= amount
                target_cash += amount
            users_memory[target_index] = f"{target_first} {target_last} {target_birth} {target_cash} {targeting}\n"
            with open(users_database, "w", encoding="UTF-8") as file:
                file.writelines(users_memory)
            with open(account_database, "w", encoding="UTF-8") as file:
                file.write(f"{first} {last} {birth} {user_cash} {accID}\n")
            print("Transfer successful!")
            return_to_main()

        except FileNotFoundError:
            print("Something wrong.")
            return_to_main()
except ValueError:
    print("Invalid input. Returning to main menu...")
    return_to_main()