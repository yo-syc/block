import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fyp.settings')
django.setup()

from certificates.blockchain import blockchain_service
from web3 import Web3

# Transaction hash from your certificate
tx_hash = "0x148613d26904221dec79beee1d5b650518e456b66d3589ce31957fcb1896a021"

print("\n" + "="*70)
print("DECODING BLOCKCHAIN CERTIFICATE DATA")
print("="*70)
print(f"Transaction Hash: {tx_hash}")
print()

try:
    # Get transaction from blockchain
    tx = blockchain_service.w3.eth.get_transaction(tx_hash)
    
    print(f"From: {tx['from']}")
    print(f"To: {tx['to']}")
    print(f"Block Number: {tx['blockNumber']}")
    print(f"Gas Used: {tx['gas']}")
    
    # Decode the input data
    input_data = tx['input']
    print(f"\nRaw Input Data (Hex): {input_data.hex()}")
    
    # Convert hex to text
    decoded_text = blockchain_service.w3.to_text(input_data)
    print(f"\nDecoded Certificate Data:")
    print("-" * 70)
    print(decoded_text)
    print("-" * 70)
    
    # Parse the certificate data
    if decoded_text.startswith('CERT:'):
        parts = decoded_text.split(':')
        if len(parts) >= 3:
            cert_id = parts[1]
            cert_hash = parts[2]
            
            print(f"\n✅ CERTIFICATE INFORMATION FOUND ON BLOCKCHAIN:")
            print(f"   Certificate ID: {cert_id}")
            print(f"   Certificate Hash: {cert_hash}")
            
            # Get block timestamp
            block = blockchain_service.w3.eth.get_block(tx['blockNumber'])
            from datetime import datetime
            timestamp = datetime.fromtimestamp(block['timestamp'])
            print(f"   Stored On: {timestamp}")
    else:
        print("\n⚠️ Could not parse certificate data format")
    
    print("\n" + "="*70)
    
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
