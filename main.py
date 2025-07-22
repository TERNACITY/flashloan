import time
import json
import requests
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

# === CONFIGURATION ===
RPC_URL = os.getenv("ZKSYNC_RPC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=json.loads(open('abi.json').read()))

def send_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        requests.post(url, data=payload)
    except Exception as e:
        print("Failed to send Telegram alert:", e)

def simulate_arbitrage():
    print("Scanning for arbitrage...")
    # Simulate real-time pricing data
    price_a = 100
    price_b = 105
    diff = price_b - price_a

    if diff > 4:
        print("🟢 Arbitrage opportunity found! Executing trade...")
        send_alert("🚀 Arbitrage Executed! +$5 Profit")
        # Simulate gas-free execution via Paymaster
    else:
        print("🔴 No opportunity. Waiting...")

while True:
    simulate_arbitrage()
    time.sleep(15)
