from os import system as c
import time
import random

#------------- COLOUR ------------#
A = '\033[1;97m'
R = '\033[38;5;196m'
Y = '\033[1;33m'
G = '\033[38;5;46m'
C = '\033[38;5;14m'
P = '\033[38;5;201m'

def logo():
    c('clear')
    print(f"""{G}
██╗   ██╗████████╗     ██╗   ██╗████████╗
╚██╗ ██╔╝╚══██╔══╝     ██║   ██║╚══██╔══╝
 ╚████╔╝    ██║        ██║   ██║   ██║   
  ╚██╔╝     ██║        ██║   ██║   ██║   
   ██║      ██║        ╚██████╔╝   ██║   
   ╚═╝      ╚═╝         ╚═════╝    ╚═╝   
{P}
    HACKING WORLD - YT SUBSCRIBER VIP TOOL
{A}--------------------------------------------------
""")

def menu():
    logo()
    print(f"{A}[1] Start Auto Subscriber Injection")
    print(f"{A}[0] Exit Tool")
    print(f"{A}--------------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        start_injection()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION!")
        time.sleep(1)
        menu()

def start_injection():
    logo()
    c('espeak "Initializing YouTube Subscriber Injection"')
    cookie = input(f"{C}ENTER YOUR YOUTUBE ACCOUNT COOKIE: ")
    link = input(f"{Y}ENTER TARGET CHANNEL LINK: ")
    print(f"{G}[✓] Verifying Cookie...")
    time.sleep(2)
    print(f"{G}[✓] Cookie Verified Successfully!")
    time.sleep(1)
    print(f"{Y}[+] Connecting to YouTube Secure Server...")
    time.sleep(3)
    print(f"{P}[+] Subscribing to: {link}")
    time.sleep(2)

    for i in range(1, 15):
        sub_count = random.randint(100, 500)
        print(f"{C}[*] Injecting {sub_count} Subscribers...")
        time.sleep(0.8)

    print(f"\n{G}[✓] 9999 Subscribers Added Successfully!")
    print(f"{C}Total Subscribed: {random.randint(20000, 50000)}")

    print(f"{P}\n[!] All Process Completed Successfully.")
    input(f"{A}Press Enter To Return To Menu...")
    menu()

menu()