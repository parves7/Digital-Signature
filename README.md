# 🔐 Quantum-Safe Digital Signature with Dilithium5 (Open Quantum Safe)

This project implements **post-quantum digital signatures** using the **Dilithium5** algorithm from the [Open Quantum Safe (liboqs)](https://openquantumsafe.org/) library.  
It allows you to **generate**, **sign**, and **verify** data files securely using quantum-resistant cryptography.

---

## 🧠 Features
- Uses **Dilithium5**, one of the NIST-recommended lattice-based digital signature schemes.
- Supports **SHA3-512 hashing** for message digest generation.
- Easy-to-use **file-based workflow** for signing and verification.
- Automatically regenerates signatures if verification fails.
- Quantum-safe and forward-compatible with next-generation cryptography standards.

---

## ⚙️ Requirements

- Python 3.8 or higher  
- Open Quantum Safe Python bindings (`liboqs-python`)

---

## 🧩 Installation

You can install the `liboqs-python` library either through pip (if available) or by building it from source.

### 🔹 Install using pip
```bash
pip install liboqs-python
```

### 🔹 Install from source
```bash
git clone https://github.com/open-quantum-safe/liboqs-python.git
cd liboqs-python
python setup.py install
```

---

## 🚀 How to Use

### 1️⃣ Generate a Digital Signature

Run the main script:
```bash
python main.py
```
When prompted:
```
Do you want to generate the signature: y
Enter the data file for signature generation: data.txt
```
This creates:
```
signature.bin
public_key.bin
```

These files contain the **signature** and **public key** generated using Dilithium5.

---

### 2️⃣ Verify a Digital Signature

To verify the integrity and authenticity of a file:
```
Do you want to verify the signature: y
Enter the data file for signature verification: data.txt
Enter the signature file: signature.bin
Enter the public key file: public_key.bin
```
If the file has not been modified, the program will display:
```
Digital Signature verified as Valid
```
Otherwise, it will report it as **Invalid**.

---

## 🧠 How It Works

1. The data is read from the input file.
2. A **SHA3-512 hash** is generated from the data.
3. Using the **Dilithium5** algorithm from Open Quantum Safe, the hash is signed.
4. The signature and public key are stored in binary files.
5. For verification, the program checks if the given signature matches the original hash using the provided public key.

---

## 🧩 Code Example

```python
import oqs

with oqs.Signature("Dilithium5") as algo:
    public_key = algo.generate_keypair()
    data = b"Example data"
    signature = algo.sign(data)

    if algo.verify(data, signature, public_key):
        print("Signature Verified ✅")
    else:
        print("Signature Invalid ❌")
```

---

## 📁 File Structure

```
├── main.py               # Main script for signing and verification
├── data.txt              # Input data file
├── signature.bin         # Generated signature file
├── public_key.bin        # Public key used for verification
├── README.md             # Project documentation (this file)
```

---

## 👨‍💻 Author

**Parvesh Gudivada**  
🔗 [LinkedIn](https://www.linkedin.com/in/parvesh-gudivada)  
📧 gparveshgparvesh929@gmail.com  

---

## 🛡️ License

This project is released under the **MIT License**.  
You are free to use, modify, and distribute it with attribution.

---

## 🌟 Acknowledgments

- [Open Quantum Safe Project](https://openquantumsafe.org/)
- [CRYSTALS-Dilithium Specification](https://pq-crystals.org/dilithium/)
- [NIST Post-Quantum Cryptography Standardization](https://csrc.nist.gov/projects/post-quantum-cryptography)
