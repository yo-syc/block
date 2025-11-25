import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fyp.settings')
django.setup()

from certificates.models import Certificate
from certificates.blockchain import blockchain_service

# Get certificate ID from user
cert_id = input("Enter Certificate ID (e.g., CERT-2025-BA787FDC): ").strip()

try:
    cert = Certificate.objects.get(certificate_id=cert_id)
    
    print("\n" + "="*60)
    print(f"CERTIFICATE: {cert.certificate_id}")
    print("="*60)
    print(f"Student: {cert.student_name}")
    print(f"Course: {cert.course_name}")
    print(f"Issue Date: {cert.issue_date}")
    print(f"Status: {cert.status}")
    print(f"Certificate Hash: {cert.certificate_hash}")
    
    if cert.blockchain_tx_hash:
        print(f"\n✅ BLOCKCHAIN VERIFIED!")
        print(f"Transaction Hash: {cert.blockchain_tx_hash}")
        print(f"\nView on Etherscan:")
        print(f"https://sepolia.etherscan.io/tx/{cert.blockchain_tx_hash}")
        
        # Verify on blockchain
        print("\n" + "-"*60)
        print("VERIFYING ON BLOCKCHAIN...")
        print("-"*60)
        
        try:
            is_valid, result = blockchain_service.verify_certificate_hash(cert.blockchain_tx_hash)
            
            if is_valid and isinstance(result, dict):
                print(f"✅ Transaction Found on Blockchain!")
                print(f"Block Number: {result.get('block_number', 'N/A')}")
                print(f"Stored Certificate ID: {result.get('certificate_id', 'N/A')}")
                print(f"Stored Certificate Hash: {result.get('certificate_hash', 'N/A')}")
                
                # Verify data matches
                if result['certificate_id'] == cert.certificate_id and result['certificate_hash'] == cert.certificate_hash:
                    print("\n✅✅✅ BLOCKCHAIN DATA MATCHES DATABASE! ✅✅✅")
                    print("Certificate is authentic and tamper-proof!")
                else:
                    print("\n⚠️ WARNING: Blockchain data doesn't match database!")
            else:
                print(f"❌ Blockchain verification failed: {result}")
        except Exception as e:
            print(f"❌ Error verifying: {str(e)}")
    else:
        print(f"\n⚪ Not stored on blockchain")
    
    print("="*60 + "\n")
    
except Certificate.DoesNotExist:
    print(f"\n❌ Certificate {cert_id} not found!\n")
