import os
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

SECRET_KEY = b'MySecretKey12345'  # 16-byte key

def encrypt_file(file_path):
    iv = os.urandom(16)
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    
    with open(file_path, 'rb') as f:
        data = f.read()
    
    encrypted_data = iv + cipher.encrypt(pad(data, AES.block_size))
    enc_file_path = file_path + ".enc"
    
    with open(enc_file_path, 'wb') as f:
        f.write(encrypted_data)
        
    return enc_file_path

def upload_to_ipfs(file_path):
    url = 'http://127.0.0.1:5001/api/v0/add'
    with open(file_path, 'rb') as f:
        response = requests.post(url, files={'file': f})
        
    if response.status_code == 200:
        return response.json()['Hash']
    else:
        raise Exception("IPFS Node ఆన్‌లో లేదు!")

if __name__ == "__main__":
    pdf_filename = "Akshaya Resume.pdf"

    print(f"[1] Encrypting PDF file ({pdf_filename})...")
    enc_path = encrypt_file(pdf_filename)

    print("[2] Uploading Encrypted PDF to IPFS Network...")
    try:
        cid = upload_to_ipfs(enc_path)
        print("\n================ SUCCESS ================")
        print(f"CID        : {cid}")
        print(f"Secret Key : {SECRET_KEY.decode()}")
        print("=========================================")
    except Exception as e:
        print(f"\n[Error] {e}")
