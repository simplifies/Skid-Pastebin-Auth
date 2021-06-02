import requests, os, uuid, hashlib
from colorama import Fore, init

# Declare init() so that colorama works correctly
init()

# Start of Configuration
hwid = hashlib.sha224(str(uuid.getnode()).encode()).hexdigest() + 'HWID' + hashlib.sha3_512(os.name.encode()).hexdigest()
url = 'https://pastebin.com/raw/'
# End of Configuration

# Input the username that will be later used in the auth
username = input('Username\n > ')

# Check if any of the lines of the file requested equals to "username | hwid"
if any(line.strip('\n') == f"{username} | {hwid}" for line in requests.get(url).text.split('\n')):
    # If any of the lines equals to "username | hwid" allow them inside and give them an alert
    print(f'{Fore.GREEN}[Auth] {Fore.RESET}Sucesfully authenticated')
    # Add an input and tell them to press enter to continue 
    input(f'{Fore.GREEN}[Auth] {Fore.RESET}Press enter to continue\n')
else:
    # Tell them that they failed to authenticate
    print(f'{Fore.RED}[Auth] {Fore.RESET}Failed to authenticate')
    # Give them an input and then exit the program
    input(f'{Fore.RED}[Auth] {Fore.RESET}Press enter to quit\n')
    # Quit the program
    os._exit(0)

# Enter your code here
print('Welcome!')
