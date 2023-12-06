from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

def generate_key():
    return get_random_bytes(32)  # 256 bits key for AES-256

def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_CBC)
    output_file_path = file_path + ".enc"

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file_path, 'wb') as file:
        file.write(cipher.iv + ciphertext)

    return output_file_path

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        data = file.read()

    iv = data[:AES.block_size]
    ciphertext = data[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

    output_file_path = encrypted_file_path[:-4]  # Remove the '.enc' extension

    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)

    return output_file_path

def main():
    file_path = input("Enter the path of the file: ")
    key = generate_key()

    # Encrypt the file
    encrypted_file_path = encrypt_file(file_path, key)
    print(f"File encrypted successfully. Encrypted file: {encrypted_file_path}")

    # Decrypt the file
    decrypted_file_path = decrypt_file(encrypted_file_path, key)
    print(f"File decrypted successfully. Decrypted file: {decrypted_file_path}")

if __name__ == "__main__":
    main()
