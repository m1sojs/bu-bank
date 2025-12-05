import os, sys
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear_console()
print("""
██████╗░██╗░░░██╗  ██████╗░░█████╗░███╗░░██╗██╗░░██╗  ░███████╗
██╔══██╗██║░░░██║  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝  ██╔██╔══╝
██████╦╝██║░░░██║  ██████╦╝███████║██╔██╗██║█████═╝░  ╚██████╗░
██╔══██╗██║░░░██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗░  ░╚═██╔██╗
██████╦╝╚██████╔╝  ██████╦╝██║░░██║██║░╚███║██║░╚██╗  ███████╔╝
╚═════╝░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚══════╝░
""")

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
        if not account.strip():
            raise FileNotFoundError
        for line in account:
            first, last, birth, cash, accID = account.split(" ", 4)
        
        print(f'{"Welcome back "+first + " " + last + "!":^62}')
        print(f'{"ยอดเงินคงเหลือในบัญชีของคุณ: ฿"+cash:^62}')
        
        print(f'\nSelect Mode:\n{"[1] โอนเงิน":<25} [2] ถอนเงิน \n{"[3] ฝากเงิน":<25} [4] ข้อมูลบัญชี \n[5] ปิดโปรแกรม')
        try:
            mode = int(input("►  "))
            
            if mode == 1:
                clear_console()
                import func.transfer
            elif mode == 2:
                clear_console()
                import func.withdraw
            elif mode == 3: 
                clear_console()
                import func.deposit
            elif mode == 4:
                clear_console()
                import func.accountinfo
            elif mode == 5:
                clear_console()
                exit()
            else:
                print("Invalid selection. Returning to main menu.")
                time.sleep(1)
                import main
        except ValueError:
            import main
except FileNotFoundError:
    print("Account not found. Would you like to create a new account? [1] Register  [2] Exit")
    try:
        choice = int(input("►  "))
        if choice == 1:
            clear_console()
            import func.register
        else:
            print("Exiting program.")
            time.sleep(1)
            clear_console()
            exit()
    except ValueError:
        print("Invalid input. Please try again.")
        time.sleep(1)
        import main