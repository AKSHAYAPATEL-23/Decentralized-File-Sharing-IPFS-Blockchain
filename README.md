Decentralized File Sharing System via IPFS & Blockchain

A secure, peer-to-peer file sharing and storage platform utilizing **IPFS (InterPlanetary File System)** and **Ethereum Smart Contracts** for immutable access control and tamper-proof storage.

---

## ✨ Key Features & Enhancements (v2.0)

- Immutable Storage: Stores large documents/files on IPFS while referencing cryptographic content hashes (CIDs) on the ledger.
-Blockchain Access Control: Handles file access permissions securely using smart contracts.
- Local File Encryption: Encrypts sensitive documents client-side prior to IPFS upload.
- Automated Verification:Ensures data integrity by matching hash records directly against the chain.

---

 🛠️ Tech Stack

- Language: Python
- Decentralized Storage: IPFS (InterPlanetary File System)
- Blockchain Framework:Web3 / Ethereum Smart Contracts
- Encryption: PyCryptodome / Cryptography

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/AKSHAYAPATEL-23/Decentralized-File-Sharing-IPFS-Blockchain.git](https://github.com/AKSHAYAPATEL-23/Decentralized-File-Sharing-IPFS-Blockchain.git)
   cd Decentralized-File-Sharing-IPFS-Blockchain
Install requirements:

Bash
pip install -r requirements.txt
Run Sender script:

Bash
python sender.py
Run Receiver script:

Bash
python receiver.py