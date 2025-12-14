from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

# فتح private key الموجود عندك
private_key = RSA.import_key(open("keys/private.pem").read())
cipher_rsa = PKCS1_OAEP.new(private_key)

# فتح AES key المشفّر
with open("keys/session_key.enc", "rb") as f:
    enc_session_key = f.read()

session_key = cipher_rsa.decrypt(enc_session_key)

# فتح الملف المشفّر
with open("sample.txt.enc", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce=nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)

# حفظ الملف بعد فك التشفير
with open("sample_decrypted.txt", "wb") as f:
    f.write(data)

print("File decrypted successfully!")
