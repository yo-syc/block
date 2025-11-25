import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fyp.settings')
django.setup()

from certificates.models import Certificate
from certificates.blockchain import blockchain_service

cert_id = "CERT-2025-BA787FDC"

print("\n" + "="*70)
print("CERTIFICATE VERIFICATION - DATABASE vs BLOCKCHAIN")
print("="*70)

try:
    # Get certificate from database
    cert = Certificate.objects.get(certificate_id=cert_id)
    
    print(f"\n📄 CERTIFICATE DATA (From Database):")
    print("-" * 70)
    print(f"Certificate ID: {cert.certificate_id}")
    print(f"Student Name: {cert.student_name}")
    print(f"Student Email: {cert.student_email}")
    print(f"Course Name: {cert.course_name}")
    print(f"Grade: {cert.grade}")
    print(f"Issue Date: {cert.issue_date}")
    print(f"Institution: {cert.institution_name}")
    print(f"Issued By: {cert.issued_by.username}")
    print("-" * 70)
    
    print(f"\n🔐 HASH VERIFICATION:")
    print("-" * 70)
    print(f"Database Certificate Hash: {cert.certificate_hash}")
    
    if cert.blockchain_tx_hash:
        # Get data from blockchain
        is_valid, result = blockchain_service.verify_certificate_hash(cert.blockchain_tx_hash)
        
        if is_valid and isinstance(result, dict):
            blockchain_hash = result['certificate_hash']
            print(f"Blockchain Certificate Hash: {blockchain_hash}")
            
            print(f"\n📊 COMPARISON:")
            print("-" * 70)
            if cert.certificate_hash == blockchain_hash:
                print("✅✅✅ HASHES MATCH! ✅✅✅")
                print("\n🎉 This proves:")
                print("   • Certificate data has NOT been modified")
                print("   • Certificate is AUTHENTIC")
                print("   • Database and blockchain are SYNCHRONIZED")
                print("   • Certificate is TAMPER-PROOF")
            else:
                print("❌ HASHES DO NOT MATCH!")
                print("⚠️ Warning: Certificate may have been tampered with!")
        else:
            print("❌ Could not retrieve data from blockchain")
    else:
        print("⚪ Certificate not stored on blockchain")
    
    print("\n💡 WHY WE USE SHA-256:")
    print("-" * 70)
    print("SHA-256 is a ONE-WAY hash function:")
    print("  • Cannot be reversed (hash → original data) ❌")
    print("  • Same input always gives same hash ✅")
    print("  • Tiny change in input = completely different hash ✅")
    print("  • Cryptographically secure ✅")
    print("\nWe store the HASH on blockchain (32 bytes)")
    print("Instead of full certificate data (hundreds of bytes)")
    print("This saves money on blockchain gas fees!")
    
    print("\n🔍 TO VERIFY A CERTIFICATE:")
    print("-" * 70)
    print("1. Get certificate data from database")
    print("2. Calculate SHA-256 hash of the data")
    print("3. Get stored hash from blockchain")
    print("4. Compare: Database hash == Blockchain hash?")
    print("5. If YES ✅ = Certificate is authentic and unchanged")
    print("6. If NO  ❌ = Certificate has been tampered with")
    
    print("\n" + "="*70 + "\n")
    
except Certificate.DoesNotExist:
    print(f"\n❌ Certificate {cert_id} not found!\n")
except Exception as e:
    print(f"\n❌ Error: {str(e)}\n")
    import traceback
    traceback.print_exc()
