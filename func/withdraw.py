print("""
██████╗░██╗░░░██╗  ██████╗░░█████╗░███╗░░██╗██╗░░██╗  ░███████╗
██╔══██╗██║░░░██║  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝  ██╔██╔══╝
██████╦╝██║░░░██║  ██████╦╝███████║██╔██╗██║█████═╝░  ╚██████╗░
██╔══██╗██║░░░██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗░  ░╚═██╔██╗
██████╦╝╚██████╔╝  ██████╦╝██║░░██║██║░╚███║██║░╚██╗  ███████╔╝
╚═════╝░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚══════╝░
""")

import qrcode_terminal
import time

try:
    amount = float(input("Enter amount to withdraw: ฿"))
    if amount <= 0:
        print("Invalid amount. Returning to main menu.")
        time.sleep(1)
        import main
    qrcode_terminal.draw(amount)
    print(f"\nกรุณานำ QR Code นี้ไปใช้ที่ตู้ ATM หรือ Mobile Banking เพื่อทำรายการถอนเงินจำนวน ฿{amount} ครับ/ค่ะ")
    input("\nEnter to return to main menu...")
    import main
except ValueError:
    print("Error generating QR code.")
    time.sleep(1)
    import main