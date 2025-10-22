import hashlib
import os 
import oqs

def data_file_reader(file_path,mode="rb"):
    try:
        with open(file_path, mode) as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def data_file_writer(data,file_path,mode="wb"):
    try:
        with open(file_path, mode) as file:
            file.write(data)
        print(f"Successfully wrote to {file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")    

def hasher(a):
    s=hashlib.sha3_512()
    s.update(a)
    return s.digest()

def encrypt(data):
    with oqs.Signature("Dilithium5") as Algo:
        public_key=Algo.generate_keypair()
        signature=Algo.sign(data)
        if Algo.verify(data, signature, public_key):
            return signature, public_key
        else:
            return encrypt(data)
    
def verifier(data,signature,public_key):
    with oqs.Signature("Dilithium5") as Algo:
        return Algo.verify(data,signature,public_key)

if __name__=='__main__':
    D=input("Do to you want to generate the signature:").lower()
    if D=='y':
        data_path=input("Enter the data file for signature genration:")
        data=data_file_reader(data_path)
        s=hasher(data)
        signature,public_key=encrypt(s)
        data_file_writer(signature,'signature.bin')
        data_file_writer(public_key,'public_key.bin')
        D = 'N'

    D=input("Do you want to verify the signature:").lower()
    if D=='y':
        data_path=input("Enter the data file for signature verification:")
        data=data_file_reader(data_path)
        s=hasher(data)
        signature_path=input("Enter the signature file:")
        signature=data_file_reader(signature_path)
        public_key_path=input("Enter the public key file:")
        public_key=data_file_reader(public_key_path)
        print(("Digital Signature verified as Valid" if verifier(s,signature,public_key) else "Digital Signature verified as Invalid"))
