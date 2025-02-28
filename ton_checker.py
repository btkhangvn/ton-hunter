import requests
import random
import binascii
import time
from colorama import init, Fore, Style

# Initialize colorama (for Windows compatibility)
init(autoreset=True)

TON_API_URL = "https://toncenter.com/api/v2/getAddressBalance"
API_KEY = "1e2dc49db692e4fd8e311d5891244de0c8b03a3abb6777834218ebac8adb8a66"  # Replace with your API key

def generate_ton_address():
    """Generate a fake TON address with a random private key (mock example)"""
    private_key = binascii.hexlify(random.randbytes(32)).decode()  # Random private key
    public_key = binascii.hexlify(random.randbytes(32)).decode()   # Random public key
    address = f"EQ{public_key[:64]}" 

    return private_key, address

def get_ton_balance(address):
    """Check balance of a TON address using Toncenter API"""
    params = {"address": address}
    if API_KEY:
        params["api_key"] = API_KEY
    try:
        response = requests.get(TON_API_URL, params=params)
        data = response.json()
        if "result" in data:
            return int(data["result"]) / 1e9  # Convert from nanoTON to TON
    except Exception as e:
        print(Fore.RED + f"❌ Error checking balance for {address}: {e}")
    return 0

def main():
    """Continuously generate TON addresses, check balance, and save non-empty ones"""
    with open("valid_ton_addresses.txt", "a") as file:
        while True:
            private_key, address = generate_ton_address()
            balance = get_ton_balance(address)

            # Print the results with colors
            print(Fore.CYAN + "🔹 Generated Address: " + Fore.YELLOW + address)
            print(Fore.CYAN + "🔑 Private Key: " + Fore.GREEN + private_key)
            print(Fore.MAGENTA + f"💰 Balance: {balance} TON")

            # Save only non-empty addresses
            if balance > 0:
                result = f"{address}: {balance} TON (Private Key: {private_key})\n"
                file.write(result)
                file.flush()
                print(Fore.GREEN + f"✅ Found non-empty address: {result}")

            print(Fore.BLUE + "-" * 50)  # Separator for readability
            time.sleep(0.3)  # Delay to avoid API rate limits

if __name__ == "__main__":
    main()
