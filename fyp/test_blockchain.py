import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fyp.settings')
django.setup()

from certificates.blockchain import blockchain_service
from web3 import Web3

print("=" * 50)
print("BLOCKCHAIN CONNECTION TEST")
print("=" * 50)

# Check connection
connected = blockchain_service.is_connected()
print(f"✓ Connected: {connected}")

# Get account
account = blockchain_service.get_account()
print(f"✓ Account: {account}")

# Get balance
if account:
    balance = blockchain_service.w3.eth.get_balance(account)
    balance_eth = Web3.from_wei(balance, 'ether')
    print(f"✓ Balance: {balance_eth} ETH")
    
    if balance == 0:
        print("\n⚠ WARNING: Account has 0 ETH!")
        print("⚠ You funded a different address: 0x29fe00B1CF3C86403BB3B346B0DcAbD5B9ECc595")
        print(f"⚠ But your private key maps to: {account}")
        print("\nSOLUTION: Send Sepolia ETH to the correct address:")
        print(f"https://sepoliafaucet.com/")
        print(f"Address to fund: {account}")
    else:
        print("\n✅ Blockchain is ready! You can issue certificates now.")

print("=" * 50)
