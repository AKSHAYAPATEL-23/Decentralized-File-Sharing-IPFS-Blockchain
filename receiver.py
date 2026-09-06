import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def fetch_from_ipfs(cid):
    local_gateway_url = f"http://127.0.0.1:8080/ipfs/{cid}"
    print(f"[1] Fetching encrypted PDF from IPFS ({local_gateway_url})...")
    
    try:
        response = requests.get(local_gateway_url, timeout=10)
        if response.status_code == 200:
            return response.content
    except Exception:
        pass

    api_url = f"http://127.0.0.1:5001/api/v0/cat?arg={cid}"
    response = requests.post(api_url, timeout=10)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("డేటా పొందడంలో విఫలమైంది.")

def decrypt_file(encrypted_data, secret_key, output_filename):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    original_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    

    with open(output_filename, 'wb') as f:
        f.write(original_data)
        
    print(f"[2] Decryption successful! PDF saved as: {output_filename}")

if __name__ == "__main__":
    user_cid = input("Enter IPFS CID: ").strip()
    user_key = input("Enter Secret Key (16 chars): ").strip().encode()

    try:
        enc_data = fetch_from_ipfs(user_cid)
        # ఇక్కడ PDF పేరుతో సేవ్ అవుతుంది
        decrypt_file(enc_data, user_key, "downloaded_file.pdf") 
        print("\nమీ ఫోల్డర్‌లో 'downloaded_file.pdf' క్రియేట్ అయ్యింది. దాన్ని ఓపెన్ చేసి చూడవచ్చు!")
    except Exception as e:
        print(f"\n[Error] {e}")
