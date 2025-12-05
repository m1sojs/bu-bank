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
    import main

def resource_path(relative_path): 
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generate_account_id():
    import random
    return str(random.randint(10000000, 99999999))

print("Creating account", end="", flush=True)
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
firstname = input("\nEnter your first name: ")
lastname = input("Enter your last name: ")
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

path = resource_path("database/account.txt")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="UTF-8") as file:
    file.write(f"{firstname} {lastname} {birthdate} 0 {generate_account_id()}\n")
    
path = resource_path("database/users.txt")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="UTF-8") as file:
    for i in range(5):
        file.write(f"{generate_account_id()} {generate_account_id()} {generate_account_id()} 0 {generate_account_id()}\n")

print("Generating account, Please wait", end="", flush=True)
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print("\nAccount created successfully!")
time.sleep(2)

return_to_main()

    
